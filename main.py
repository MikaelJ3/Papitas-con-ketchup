from flask import Flask, jsonify, request
from handler.people import peopleHandler
from handler.product import producthandler
from handler.request import RequestHandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello, Welcome to: Ayuda pal Jibaro! A backend system for disaster site resources locator'


# OK
'''GET ALL PRODUCTS'''


@app.route('/products', methods=['GET', 'POST'])
def getAllProducts():
    if request.method == 'POST':
        return producthandler().insert_product(request.form)  # insert a product
    else:
        if not request.args:
            return producthandler().get_all_products()  # gets all products by product name
        else:
            return producthandler().search_products(request.args)  # filter products by product attributes

# @app.route('/register', methods=['POST'])
# def Register():
#     peopleHandler().add_user()
#     return redirect(url_for('user_home')
#
# @app.route('/register/address', methods=['POST'])
# def Register():
#     peopleHandler().add_user()
#     return redirect(url_for('user_home')

@app.route('/products/supplier')
def get_products_by_supplier():
    if not request.args:
        return peopleHandler().get_all_products_by_supplier()  # gets all products by product name, grouped by supplier id
    else:
        return peopleHandler().getProductsBySupplier(request.args)  # filters products by supplier id, first name, full name



@app.route('/products/city')
def get_products_by_city():
    if not request.args:
        return peopleHandler().get_all_products_by_city(request.args)  # gets all products by product name, grouped by city
    else:
        return peopleHandler().get_all_products_by_city(request.args)  # filters products by city


@app.route('/products/zipcode')
def get_products_by_zipcode():
    if not request.args:
        return peopleHandler().get_all_products_by_zipcode(request.args)  # gets all products by product name, grouped by city
    else:
        return peopleHandler().get_all_products_by_zipcode(request.args)  # filters products by city


@app.route('/products/country')
def get_products_by_country():
    if not request.args:
        return peopleHandler().get_all_products_by_country(request.args)  # gets all products by product name, grouped by city
    else:
        return peopleHandler().get_all_products_by_country(request.args)  # filters products by city


@app.route('/PIN/FirstName')
def getPINByFirstName():
    if not request.args:
        return peopleHandler().getAllPeopleInNeed()
    else:
        return peopleHandler().getPINByFirstName(request.args)

##################### N E W ############################################################################################


# # #  A D M I N I S T R A T O R  # # #

@app.route('/admins', methods=['GET', 'POST'])
def getAllAdmin():
    if request.method == 'POST':
        return peopleHandler().insert_admin(request.form)
    else:
        if not request.args:
            return peopleHandler().getAllAdmin()
        else:
            return peopleHandler().searchADMINByRequests(request.args)

# # #  P E O P L E  I N  N E E D  # # #

@app.route('/pin', methods=['GET', 'POST'])
def getAllpin():
    if request.method == 'POST':
        return peopleHandler().insert_pin(request.form)
    else:
        if not request.args:
            return peopleHandler().getAllpin()
        else:
            return peopleHandler().searchPINByRequests(request.args)

# # #  S U P P L I E R  # # #

@app.route('/supplier', methods=['GET', 'POST'])
def getAllSUP():
    if request.method == 'POST':
        return peopleHandler().insert_sup(request.form)
    else:
        if not request.args:
            return peopleHandler().getAllsup()
        else:
            return peopleHandler().searchSUPByRequests(request.args)


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


# OK
'''FIND PRODUCT BY DISTRICT'''


@app.route('/AyudaPalJibaro/products/district')
def findSpecificProduct():
    if not request.args:
        return producthandler().getAllProducts()
    else:
        return producthandler().findSpecificProduct(request.args)


'''GET ALL PEOPLE IN NEED'''


@app.route('/AyudaPalJibaro/ShowAllPeopleInNeed')
def getAllPIN():
    return peopleHandler().getAllPeopleInNeed()


'''GET ALL SUPPLIERS'''


@app.route('/AyudaPalJibaro/ShowAllSuppliers')
def getAllSuppliers():
    return peopleHandler().getAllSuppliers()


'''GET ALL ADMIN'''





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

if __name__ == '__main__':
    app.run()