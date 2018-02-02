from flask import Flask, request, render_template, flash, redirect, url_for, jsonify
from flask_login import login_manager, current_user, login_user, logout_user
from handler.people import peopleHandler
from handler.product import producthandler
from handler.request import RequestHandler
from handler.orders import OrdersHandler
from Forms.SigninForm import LoginForm
from Forms.SignupForm import SignupForm
from Forms.user import User
import copy
import temp_DB_and_cart

app = Flask(__name__)
lm = login_manager.LoginManager()
app.secret_key = 'medalla base'
lm.init_app(app)
lm.login_view = 'SignIn'
temp_Dicts = temp_DB_and_cart.Create()

@lm.user_loader
def load_user(user_id):
    return User().get_user(user_id)


@app.route('/')
def home():
    if current_user.is_anonymous:
        return render_template('home.html')
    else:
        return redirect(url_for('user_home'))


@app.route('/UserHome')
def user_home():
    return render_template('user_home.html', account=current_user.user_type)

@app.route('/login', methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated:
       return redirect(url_for('home'))
   form = LoginForm()
   username = form.username.data
   if form.validate_on_submit():
       password = peopleHandler().login(username)
       if password is None or not password[0] == form.password.data:
           flash('Invalid username or password', category='error')
           return redirect(url_for('login'))
       user = User()
       user.set_user(username)
       login_user(user, remember=False)
       return render_template('user_home.html', title='logged in')
   return render_template('login.html', title='Sign In', form=form)


@app.route('/SignUp', methods=['GET', 'POST'])
def signup():
   form = SignupForm()
   if form.validate_on_submit():
       username = form.username.data
       password = form.password.data
       fname = form.fname.data
       lname = form.lname.data
       phone = form.phone.data
       address = form.address.data
       city = form.city.data
       country = form.country.data
       district = form.district.data
       zipcode = form.zipcode.data
       user_type = form.user_type.data
       check_if_taken = peopleHandler().login(username)
       if check_if_taken:
           flash('That username is already taken', category='error')
           return redirect(url_for('signup'))
       signed_up = peopleHandler().signup(username, password, fname, lname, phone, address, city, district,
                                          country, zipcode, user_type)
       if not signed_up:
           flash('Signed Up Failed')
           return redirect(url_for('signup'))
       user = User()
       user.set_user(username)
       login_user(user, remember=False)
       return render_template('base.html', title='signed up')
   return render_template('signup.html', title='Sign Up', form=form)


@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('home'))

########################################################################################################################

# # #  A D M I N I S T R A T O R  # # #

@app.route('/AyudaPalJibaro/admin', methods=['GET', 'POST'])
def getAllAdmin():
    if request.method == 'POST':
        return peopleHandler().insert_admin(request.form)
    else:
        if not request.args:
            return peopleHandler().getAllAdmin()
        else:
            return peopleHandler().searchADMINByRequests(request.args)

@app.route('/AyudaPalJibaro/request/change/<int:r_id>', methods=['PUT', 'DELETE'])
def requestChange(r_id):
    if request.method == 'PUT':
        return RequestHandler().updateRequest(r_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

# # #  R E Q U E S T S # # #

@app.route('/AyudaPalJibaro/request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        return RequestHandler().insert_request(request.form)
    else:
        if not request.args:
            return RequestHandler().getAllRequest()
        else:
            return RequestHandler().searchProductByRequests(request.args)

@app.route('/AyudaPalJibaro/request/change/<int:r_id>', methods=['PUT', 'DELETE'])
def requestChange(r_id):
    if request.method == 'PUT':
        return RequestHandler().updateRequest(r_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

'''GET ALL PEOPLE IN NEED'''
@app.route('/AyudaPalJibaro/ShowAllPeopleInNeed')
def getAllPIN():
    return peopleHandler().getAllPeopleInNeed()


'''GET ALL SUPPLIERS'''
@app.route('/AyudaPalJibaro/ShowAllSuppliers')
def getAllSuppliers():
    return peopleHandler().getAllSuppliers()


'''GET ALL ADMIN'''
@app.route('/AyudaPalJibaro/ShowAllAdmin')
def getAllAdmin():
    return peopleHandler().getAllAdminstrators()


'''GET PRODUCTS BY SUPPLIER'''
@app.route('/AyudaPalJibaro/GetProductsBySupplier')
def getProductsBySupplier():
    if not request.args:
        return producthandler().getAllProducts()
    else:
        return peopleHandler().getProductsBySupplier(request.args)


'''GET SUPPLIERS BY PRODUCT'''
@app.route('/AyudaPalJibaro/GetSupplierByProduct')
def getSupplierByProduct():
    if not request.args:
        return peopleHandler().getAllSuppliers()
    else:
        return peopleHandler().getSupplierByProduct(request.args)
@app.route('/products/addCreditCard', methods=['GET', 'POST'])
def add_creditcard():
    if request.method == 'GET':
        return render_template('Add_Payment_Method.html')
    else:
        c_cardtype = request.form['c_cardtype']
        c_name = request.form['c_name']
        c_number = request.form['c_number']
        addressid = current_user.address_id
        pin_id = current_user.person_id
        verified = peopleHandler().Verify_PaymentMethod(pin_id)
        if verified:
            result = peopleHandler().insert_new_cc(c_cardtype, c_number, c_name, pin_id, addressid)
            return render_template('New_CC_Info.html', result=result)
        else:
            flash('Method Invalid! You already have a Credit Card registered in our system!')
            return redirect(url_for('home'))

@app.route('/products/updateCreditCard', methods=['GET', 'POST'])
def update_creditcard():
    if request.method == 'GET':
        result = peopleHandler().Verify_CCExists(current_user.person_id)
        if result:
            return render_template('Update_Credit_Card.html', result=result)
        else:
            return render_template('Update_Credit_Card.html')
    else:
        c_id = request.form['c_id']
        c_cardtype = request.form['c_cardtype']
        c_name = request.form['c_name']
        c_number = request.form['c_number']
        addressid = current_user.address_id
        pin_id = current_user.person_id
        verified = peopleHandler().Verify_CCExists(pin_id)
        if verified:
            result = peopleHandler().update_cc(c_id, c_cardtype, c_number, c_name, pin_id, addressid)
            return render_template('New_CC_Info.html', result=result)
        else:
            flash('Method Invalid! You do not have a Credit Card registered in our system!')
            return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()

### U N U S E D  O R  O B S O L E T E


'''GET ORDERS BY PERSON IN NEED'''
@app.route('/AyudaPalJibaro/GetOrdersByPersonInNeed')
def getOrdersByPerson():
   if not request.args:
       return peopleHandler().getAllOrders()
   else:
       return peopleHandler().getOrdersByPersonInNeed(request.args)


'''GET ORDERS BY SUPPLIER'''
@app.route('/AyudaPalJibaro/GetOrdersBySupplier')
def getOrdersBySupplier():
   if not request.args:
       return peopleHandler().getAllOrders()
   else:
       return peopleHandler().getOrdersBySupplier(request.args)


'''GET Person in need BY First Name'''
#https://ayudapaljibaro.herokuapp.com/AyudaPalJibaro/PIN/FirstName?pin_fname=Michael
@app.route('/AyudaPalJibaro/PIN/FirstName')
def getPINByFirstName():
   if not request.args:
       return peopleHandler().getAllPeopleInNeed()
   else:
       return peopleHandler().getPINByFirstName(request.args)

'''FIND PRODUCT BY DISTRICT'''
@app.route('/AyudaPalJibaro/products/district')
def findSpecificProduct():
    if not request.args:
        return producthandler().getAllProducts()
    else:
        return producthandler().findSpecificProduct(request.args)
'''GET ALL PRODUCTS'''


@app.route('/AyudaPalJibaro/products')
def getAllProducts():
    return producthandler().getAllProducts()


# OK
'''GET PRODUCT BY ID'''
@app.route('/AyudaPalJibaro/products/<int:p_id>')
def getProductById(p_id):
    return producthandler().getProductById(p_id)


# OK
'''GET IF AVAILABLE'''
@app.route('/AyudaPalJibaro/products/availability/<int:p_id>')
def getAvailabilityOfProduct(p_id):
    return producthandler().getAvailabilityOfProduct(p_id)


# OK
'''BROWSE RESOURCES REQUESTED'''


@app.route('/AyudaPalJibaro/products/requested')
def browseResourcesRequested():
    return RequestHandler().browseResourcesRequested()


# OK
'''SEARCH AVAILABLE PRODUCTS BY ATRIBUTE'''
@app.route('/AyudaPalJibaro/products/available')
def browseResourcesAvailable():
    return producthandler().browseResourcesAvailable()

@app.route('/products/addBankInfo', methods=['GET', 'POST'])
def add_bank_info():
    return True


@app.route('/products/updateProduct', methods=['GET', 'POST'])
def update_product():
    if request.method == 'GET':
        result_list = peopleHandler().getProductsBySupplier(current_user.person_id)
        if result_list:
            return render_template('Update_Product.html', result_list=result_list)
        else:
            return render_template('Update_Product.html')
    else:
        form = request.form['p_id']
        p_id = form
        form = request.form['cat']
        c_id = form
        form = request.form['p_name']
        p_name = form
        form = request.form['r_qty']
        p_qty = form
        form = request.form['p_unit']
        p_unit = form
        form = request.form['p_priceperunit']
        p_priceperunit = form
        s_id = current_user.person_id
        verified = producthandler().VerifyID(p_id)
        if verified:
            product = producthandler().update_product(p_id, c_id, s_id, p_name, p_qty, p_unit, p_priceperunit)
            return render_template("Add_Product_Result.html", product=product)
        else:
            flash('Product Verification Failed! Try Again!')
            return redirect(url_for('Update_Product'))

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET':
        return render_template('Add_Product.html')
    else:
        ct_id = request.form['cat']
        p_name = request.form['p_name']
        p_qty = request.form['r_qty']
        p_unit = request.form['p_unit']
        p_ppu = request.form['p_ppu']
        s_id = current_user.person_id
        product = producthandler().insert_new_product(ct_id, s_id, p_name, p_qty, p_unit, p_ppu)
        return render_template('Add_Product_Result.html', product=product)


@app.route('/products/announce', methods=['GET', 'POST'])
def announce_product():
    result_list = producthandler().AnnounceAvailability()
    return render_template('test.html', result_list=result_list)


@app.route('/products/ask', methods=['GET', 'POST'])
def ask_product():
    if request.method == 'GET':
        return render_template('Request_Product.html')
    else:
        product_name = request.form['r_pname']
        quantity = request.form['r_qty']
        date = request.form['r_date']
        request_info = RequestHandler().insert_new_request(current_user.person_id, product_name, quantity, date)
        return render_template('Added_Request_Result.html', request_info=request_info)


@app.route('/products/buy', methods=['GET', 'POST'])
def buy_product():
    if request.method == 'GET':
        result = peopleHandler().Verify_CCExists(current_user.person_id)
        if result:  # Verifies if User has a credit card, cancel buy method if there isn't
            if not temp_Dicts.temp_DB:  # verifies if there's a temp array of dicts for editing and presenting
                result_list = producthandler().getPurchasableProduct()  # gets current state of DB and copies it to
                # the temp
                if result_list:
                    temp_Dicts.temp_DB = copy.deepcopy(result_list)
                    temp_Dicts.cart = []
                    return render_template('Buy_Product.html', result_list=result_list)
                else:
                    flash('You should not have gotten here unless DB is somehow empty.ABORT!')
                    return redirect(url_for('user_home'))
            else:  # presents the edited temp table on screen to reflect adding products in cart
                return render_template('Buy_Product.html', result_list=temp_Dicts.temp_DB)
        else:  # No Credit Card NO Buying for you
            flash('Credit Card needed for this operation.')
            return redirect(url_for('user_home'))
    else:
        if request.form['Button'] == 'view cart':  # shows cart on screen if that is what the user
            # desired(or misclick who knows)
            temp_Dicts.Is_it_Free = False
            return redirect(url_for('view_cart'))
        elif request.form['Button'] == 'Cancel Order':  # User got cold feet with this purchase,
            # cancels temp changes and goes back to home
            flash('Your Order has been canceled. Thank you for your patronage.')
            temp_Dicts.temp_DB = []
            temp_Dicts.cart = []
            return redirect(url_for('user_home'))
        else:
            pid = int(request.form['Button'])
            p_qty = int(request.form['product_quantity' + request.form['Button']])
            for dict_items in temp_Dicts.temp_DB:  # Looks for the product to adjust
                # left in stock to reflect the add to cart
                if dict_items['Product Id'] == pid:
                    pname = dict_items['Product Name']
                    qty = dict_items['Left in Stock']
                    dict_items['Left in Stock'] = qty - p_qty
                else:
                    continue
            another_temp = dict()  # creates an empty dictionary to store the id and quantity for the cart
            another_temp['p_id'] = pid
            another_temp['p_qty'] = p_qty
            another_temp['Product Name'] = pname
            temp_Dicts.cart.append(another_temp)  # stores recently created dictionary to temp array that is the cart
            return redirect(url_for('buy_product'))


@app.route('/products/cart', methods=['GET', 'POST'])
def view_cart():
    if request.method == 'GET':
        return render_template('view_cart.html', result_list=temp_Dicts.cart)
    else:
        if request.form['Button'] == 'Return':
            if not temp_Dicts.Is_it_Free:
                return redirect(url_for('buy_product'))
            else:
                return redirect(url_for('get_product'))
        elif request.form['Button'] == 'Cancel':
            flash('Your Order has been canceled. Thank you for your patronage.')
            temp_Dicts.temp_DB = []
            temp_Dicts.cart = []
            return redirect(url_for('user_home'))
        else:  # Here's the checkout magic
            if not temp_Dicts.cart:
                flash('You have zero products in your cart, please select a product for purchase first.')
                if not temp_Dicts.Is_it_Free:
                    return redirect(url_for('buy_product'))
                else:
                    return redirect(url_for('get_product'))
            else:
                # Aqui va la magia
                credit_card_info = peopleHandler().Verify_CCExists(current_user.person_id)
                credit_card_id = int(credit_card_info['Card ID'])
                order_id = OrdersHandler().create_new_order(credit_card_id)
                order_details_ids = []
                for dict_items in temp_Dicts.cart:
                    ordering_result = producthandler().insert_new_OrderDetails(dict_items['p_qty'], order_id,
                                                                               current_user.person_id,
                                                                               dict_items['p_id'])
                    order_details_ids.append(ordering_result)
                if not order_details_ids:
                    flash('something went wrong.')
                    return redirect(url_for('user_home'))
                else:
                    temp_Dicts.cart = []
                    temp_Dicts.temp_DB = []
                    flash('purchase is succesful, view transactions to confirm')
                    return redirect(url_for('user_home'))


@app.route('/products/getFreeProduct', methods=['GET', 'POST'])
def get_product():
    if request.method == 'GET':
        result = peopleHandler().Verify_CCExists(current_user.person_id)
        if result:  # Verifies if User has a credit card, cancel buy method if there isn't
            if not temp_Dicts.temp_DB:  # verifies if there's a temp array of dicts for editing and presenting
                result_list = producthandler().getFreeProduct()  # gets current state of DB and copies it to
                # the temp
                if result_list:
                    temp_Dicts.temp_DB = copy.deepcopy(result_list)
                    temp_Dicts.cart = []
                    return render_template('Free_Product.html', result_list=result_list)
                else:
                    flash('You should not have gotten here unless DB is somehow empty.ABORT!')
                    return redirect(url_for('user_home'))
            else:  # presents the edited temp table on screen to reflect adding products in cart
                return render_template('Free_Product.html', result_list=temp_Dicts.temp_DB)
        else:  # No Credit Card NO Buying for you
            flash('Credit Card needed for this operation.')
            return redirect(url_for('user_home'))
    else:
        if request.form['Button'] == 'view cart':  # shows cart on screen if that is what the user
            # desired(or misclick who knows)
            temp_Dicts.Is_it_Free = True
            return redirect(url_for('view_cart'))
        elif request.form['Button'] == 'Cancel Order':  # User got cold feet with this purchase,
            # cancels temp changes and goes back to home
            flash('Your Order has been canceled. Thank you for your patronage.')
            temp_Dicts.temp_DB = []
            temp_Dicts.cart = []
            return redirect(url_for('user_home'))
        else:
            pid = int(request.form['Button'])
            p_qty = int(request.form['product_quantity' + request.form['Button']])
            for dict_items in temp_Dicts.temp_DB:  # Looks for the product to adjust
                # left in stock to reflect the add to cart
                if dict_items['Product Id'] == pid:
                    pname = dict_items['Product Name']
                    qty = dict_items['Left in Stock']
                    dict_items['Left in Stock'] = qty - p_qty
                else:
                    continue
            another_temp = dict()  # creates an empty dictionary to store the id and quantity for the cart
            another_temp['p_id'] = pid
            another_temp['p_qty'] = p_qty
            another_temp['Product Name'] = pname
            temp_Dicts.cart.append(another_temp)  # stores recently created dictionary to temp array that is the cart
            return redirect(url_for('get_product'))


@app.route('/products/pin/viewtransaction', methods=['GET', 'POST'])
def view_transaction_pin():
    pin_id = current_user.person_id
    transactions = peopleHandler().getOrdersByPersonInNeed(pin_id)
    return render_template('View_Transactions.html', transactions=transactions)


@app.route('/products/supplier/viewtransaction', methods=['GET', 'POST'])
def view_transaction_sup():
    supplier = current_user.person_id
    transactions = peopleHandler().getOrdersBySupplier(supplier)
    return render_template('View_Transactions.html', transactions=transactions)



