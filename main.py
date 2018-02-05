from flask import Flask, jsonify, request
from handler.people import peopleHandler
from handler.product import producthandler
from handler.request import RequestHandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello, Welcome to: Ayuda pal Jibaro! A backend system for disaster site resources locator'


#########PRODUCTS########

#https://ayudapaljibaro.herokuapp.com/products
#https://ayudapaljibaro.herokuapp.com/products?ct_id=2

@app.route('/products', methods=['GET', 'POST'])
def get_all_products():
    if request.method == 'POST':
        return producthandler().insert_product(request.form)  # insert a product
    else:
        if not request.args:
            return producthandler().get_all_products()  # gets all products by product name
        else:
            return producthandler().search_products(request.args)  # filter products by product attributes

#https://ayudapaljibaro.herokuapp.com/products/1
@app.route('/products/<int:p_id>', methods=['GET', 'PUT', 'DELETE'])
def get_specific_product(p_id):
    if request.method == 'GET':
        return producthandler().getProductById(p_id)
    elif request.method == 'PUT':
        return producthandler().update_product(p_id, request.form)
    elif request.method == 'DELETE':
        return producthandler().delete_product(p_id)
    else:
        return jsonify(Error="Method not allowed."), 405

### F I X ##
@app.route('/products/<int:p_id>/suppliers')
def get_supplier_by_product_id(p_id):
    return peopleHandler().getSupplierByProduct(p_id)

# https://ayudapaljibaro.herokuapp.com/products/supplier
# https://ayudapaljibaro.herokuapp.com/products/supplier?s_id=1
# https://ayudapaljibaro.herokuapp.com/products/supplier?s_fname=Leia
@app.route('/products/supplier')
def get_products_by_supplier():
    if not request.args:
        return peopleHandler().get_all_products_by_supplier()  # gets all products by product name, grouped by supplier id
    else:
        return peopleHandler().getProductsBySupplier(request.args)  # filters products by supplier id, first name, full name


# https://ayudapaljibaro.herokuapp.com/products/city
# https://ayudapaljibaro.herokuapp.com/products/city?city=San Juan
@app.route('/products/city')
def get_products_by_city():
    if not request.args:
        return peopleHandler().get_all_products_by_city(request.args)  # gets all products by product name, grouped by city
    else:
        return peopleHandler().get_all_products_by_city(request.args)  # filters products by city

# https://ayudapaljibaro.herokuapp.com/products/zipcode
# https://ayudapaljibaro.herokuapp.com/products/zipcode?zipcode=00623
@app.route('/products/zipcode')
def get_products_by_zipcode():
    if not request.args:
        return peopleHandler().get_all_products_by_zipcode(request.args)  # gets all products by product name, grouped by city
    else:
        return peopleHandler().get_all_products_by_zipcode(request.args)  # filters products by city

# https://ayudapaljibaro.herokuapp.com/products/country
# https://ayudapaljibaro.herokuapp.com/products/country?country=Puerto Rico
@app.route('/products/country')
def get_products_by_country():
    if not request.args:
        return peopleHandler().get_all_products_by_country(request.args)  # gets all products by product name, grouped by city
    else:
        return peopleHandler().get_all_products_by_country(request.args)  # filters products by city

# https://ayudapaljibaro.herokuapp.com/products/district
# https://ayudapaljibaro.herokuapp.com/products/district?district=San Juan
@app.route('/products/district')
def get_products_by_district():
    if not request.args:
        return peopleHandler().get_all_products_by_district(request.args)  # gets all products by p_name, grouped by city
    else:
        return peopleHandler().get_all_products_by_district(request.args)  # filters products by city


############Transactions##################
# https://ayudapaljibaro.herokuapp.com/transactions
# https://ayudapaljibaro.herokuapp.com/transactions?s_id=2
@app.route('/transactions')
def get_all_orders():
    if not request.args:
        return peopleHandler().get_all_orders()  # gets all products by product name
    else:
        return peopleHandler().search_orders(request.args)  # filter products by product attributes

# https://ayudapaljibaro.herokuapp.com/products/buy
@app.route('/products/buy', methods=['GET', 'POST'])
def buy_product():
    if request.method == 'POST':
        return producthandler().buy_product(request.form)  # insert a product
    else:
        return producthandler().getPurchasableProduct()

# https://ayudapaljibaro.herokuapp.com/products/reserve
@app.route('/products/reserve', methods=['GET', 'POST'])
def reserve_product():
    if request.method == 'POST':
        return producthandler().buy_product(request.form)  # insert a product
    else:
        return producthandler().getFreeProduct()

# # #  A D D R E S S # # #

# https://ayudapaljibaro.herokuapp.com/address
@app.route('/address')
def getAllAddress():
    return peopleHandler().getAllAddress()

# https://ayudapaljibaro.herokuapp.com/address/update/2
@app.route('/address/update/<int:address_id>', methods=['PUT', 'DELETE'])
def addressChange(address_id):
    if request.method == 'PUT':
        return peopleHandler().updateAddresses(address_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


# # #  A D M I N I S T R A T O R  # # #
# https://ayudapaljibaro.herokuapp.com/admins
# https://ayudapaljibaro.herokuapp.com/admins?ad_fname=Manuel
@app.route('/admins', methods=['GET', 'POST'])
def get_all_admin():
    if request.method == 'POST':
        return peopleHandler().insert_admin(request.form)
    else:
        if not request.args:
            return peopleHandler().getAllAdmin()
        else:
            return peopleHandler().searchADMINByRequests(request.args)

# https://ayudapaljibaro.herokuapp.com/admins/6
@app.route('/admins/<int:ad_id>', methods=['PUT', 'GET'])
def get_specific_admin(ad_id):
    if request.method == 'GET':
        return peopleHandler().get_specific_admin(ad_id)
    elif request.method == 'PUT':
        return peopleHandler().update_admin(ad_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

########################## U S E R S ######################
# https://ayudapaljibaro.herokuapp.com/users
@app.route('/users')
def get_all_users():
    return peopleHandler().getAllUsers()


# # #  P E O P L E  I N  N E E D  # # #
# https://ayudapaljibaro.herokuapp.com/pin
# https://ayudapaljibaro.herokuapp.com/pin?pin_id=4
@app.route('/pin', methods=['GET', 'POST'])
def getAllpin():
    if request.method == 'POST':
        return peopleHandler().insert_pin(request.form)
    else:
        if not request.args:
            return peopleHandler().getAllpin()
        else:
            return peopleHandler().searchPINByRequests(request.args)

#https://ayudapaljibaro.herokuapp.com/pin/8
@app.route('/pin/<int:pin_id>', methods=['PUT', 'GET'])
def get_specific_pin(pin_id):
    if request.method == 'GET':
        return peopleHandler().get_specific_pin(pin_id)
    elif request.method == 'PUT':
        return peopleHandler().update_pin(pin_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


# # #  S U P P L I E R  # # #
# https://ayudapaljibaro.herokuapp.com/supplier
# https://ayudapaljibaro.herokuapp.com/supplier?s_id=5
@app.route('/supplier', methods=['GET', 'POST'])
def getAllSUP():
    if request.method == 'POST':
        return peopleHandler().insert_sup(request.form)
    else:
        if not request.args:
            return peopleHandler().getAllsup()
        else:
            return peopleHandler().searchSUPByRequests(request.args)

#https://ayudapaljibaro.herokuapp.com/supplier/5
@app.route('/supplier/<int:s_id>', methods=['PUT', 'GET'])
def get_specific_sup(s_id):
    if request.method == 'GET':
        return peopleHandler().get_specific_sup(s_id)
    elif request.method == 'PUT':
        return peopleHandler().update_supplier(s_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


# # #  R E Q U E S T S # # #
# https://ayudapaljibaro.herokuapp.com/request
# https://ayudapaljibaro.herokuapp.com/request?r_id=1
@app.route('/request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        return RequestHandler().insert_request(request.form)
    else:
        if not request.args:
            return RequestHandler().getAllRequest()
        else:
            return RequestHandler().searchProductByRequests(request.args)

# https://ayudapaljibaro.herokuapp.com/request/change/25
@app.route('/request/change/<int:r_id>', methods=['PUT', 'DELETE'])
def requestChange(r_id):
    if request.method == 'PUT':
        return RequestHandler().updateRequest(r_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

################ BANK INFO ################
#https://ayudapaljibaro.herokuapp.com/supplier/bankinfo

@app.route('/supplier/bankinfo', methods=['GET', 'PUT', 'POST'])
def get_all_bank_info():
    if request.method == 'GET':
        return peopleHandler().get_all_bank_info()
    elif request.method == 'POST':
        return peopleHandler().insert_bankinfo(request.form)

#https://ayudapaljibaro.herokuapp.com/supplier/bankinfo
#https://ayudapaljibaro.herokuapp.com/supplier/bankinfo/2
@app.route('/supplier/bankinfo/<int:s_id>', methods=['GET', 'PUT', 'POST'])
def view_bankinfo_by_sid(s_id):
    if request.method == 'GET':
        return peopleHandler().get_bankinfo_by_SID(s_id)
    elif request.method == 'PUT':
        return peopleHandler().update_bankinfo(s_id, request.form)


################## CREDIT CARD ############

@app.route('/pin/creditcard/<int:pin_id>', methods=['GET', 'PUT', 'POST'])
def view_creditcard_by_pin(pin_id):
    if request.method == 'GET':
        return peopleHandler().view_creditcard_by_PIN(pin_id)
    elif request.method == 'PUT':
        return peopleHandler().update_creditcard(pin_id, request.form)
    elif request.method == 'POST':
        return peopleHandler().insert_creditcard(request.form)

################# USER ACCOUNT #################
#https://ayudapaljibaro.herokuapp.com/accounts
@app.route('/accounts')
def get_account_by_username():
    return peopleHandler().get_all_accounts()

#https://ayudapaljibaro.herokuapp.com/account/2
@app.route('/account/<int:a_id>')
def search_account_by_username(a_id):
    return peopleHandler().search_account_by_a_id(a_id)

############# CATEGORIES ###########################
#https://ayudapaljibaro.herokuapp.com/categories
@app.route('/categories')
def get_categories():
    return producthandler().get_categories()

if __name__ == '__main__':
    app.run()