from flask import jsonify
from dao.product import ProductDAO
from dao.people import peopledao

class producthandler:
    def build_product(self, row):
        result = {}
        result['Product Id'] = row[0]
        result['Category'] = row[1]
        result['Supplier Id'] = row[2]
        result['Product Name'] = row[3]
        result['Left in Stock'] = row[4]
        result['Unit'] = row[5]
        result['Price Per Unit'] = '$' + str(row[6])
        return result

    def build_category(self, row):
        result = {}
        result['ct_Id'] = row[0]
        result['ct_type'] = row[1]
        result['ct_description'] = row[2]
        return result

    def build_pin_dict(self, row):
        result = {}
        result['pin_id'] = row[0]
        result['pin_fname'] = row[1]
        result['pin_lname'] = row[2]
        result['a_id'] = row[3]
        result['addressid'] = row[4]
        result['pin_phone'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['ad_id'] = row[0]
        result['ad_fname'] = row[1]
        result['ad_lname'] = row[2]
        result['a_id'] = row[3]
        result['addressid'] = row[4]
        result['s_phone'] = row[5]
        return result

    def build_addresses_dict(self, row):
        result = {}
        result['addressId'] = row[0]
        result['addressline1'] = row[1]
        result['zipcode'] = row[2]
        result['country'] = row[3]
        result['district'] = row[4]
        return result

    def build_orderdetails_dict(self, row):
        result = {}
        result['od_id'] = row[0]
        result['od_qty'] = row[1]
        result['od_price'] = row[2]
        result['o_id'] = row[3]
        result['pin_id'] = row[4]
        result['s_id'] = row[5]
        result['ba_id'] = row[6]
        result['p_id'] = row[7]
        return result


    def getAllProducts(self):
        dao = ProductDAO()
        product_list = dao.getAllProducts()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return result_list

    def getAvailabilityOfProduct(self, p_id):
        dao = ProductDAO()
        row = dao.getAvailabilityOfProduct(p_id)
        if not row:
            return jsonify(error="product not found"), 404
        else:
            print(row)
            product = self.build_product(row)
            return jsonify(Product=product)

    def getProductById(self, p_id):
        dao = ProductDAO()
        row = dao.getProductById(p_id)
        if not row:
            return jsonify(error="product not found"), 404
        else:
            product = self.build_product(row)
            return jsonify(Product=product)

    def getProductByName(self, p_name):
        dao = ProductDAO()
        row = dao.getProductByName(p_name)
        if not row:
            return jsonify(error="product not found"), 404
        else:
            product = self.build_product(row)
            return jsonify(Product=product)

    def getProductsByQuantity(self, p_qty):
        dao = ProductDAO()
        product_list = dao.getProductByQty(p_qty)
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    def findSpecificProduct(self, args):
        p_id = args.get("p_id")
        district = args.get("district")
        dao = ProductDAO()
        product_list = []
        if (len(args) == 2) and p_id and district:
            product_list = dao.findSpecificProduct(p_id, district)
        else:
            return jsonify(error="Malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    def browseResourcesAvailable(self):
        dao = ProductDAO()
        product_list = dao.browseResourcesAvailable()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    def VerifyID(self, p_id):
        dao = ProductDAO()
        row = dao.getProductById(p_id)
        if not row:
            return False
        else:
            return True

    def insert_new_product(self, cat, sid, name, qty, unit, ppu):
        dao = ProductDAO()
        pid = dao.insert_new_product(cat, sid, name, qty, unit, ppu)
        result = {}
        result['Product Id'] = pid
        result['Category'] = cat
        result['Supplier Id'] = sid
        result['Product Name'] = name
        result['Quantity'] = qty
        result['Unit'] = unit
        result['Price Per Unit'] = str(ppu) + '$'
        return result

    def update_product(self, p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit):
        dao = ProductDAO()
        p_id = dao.update_product(p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit)
        result = {}
        result['Product Id'] = p_id
        result['Category'] = ct_id
        result['Supplier Id'] = s_id
        result['Product Name'] = p_name
        result['Quantity'] = p_qty
        result['Unit'] = p_unit
        result['Price Per Unit'] = str(p_priceperunit) + '$'
        return result

    def AnnounceAvailability(self):
        dao = ProductDAO()
        product_list = dao.getAllProductsA()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return result_list

    def getPurchasableProduct(self):
        dao = ProductDAO()
        product_list = dao.getPurchasableProduct()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return result_list

    def getFreeProduct(self):
        dao = ProductDAO()
        product_list = dao.getFreeProduct()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return result_list

    def insert_new_OrderDetails(self, od_qty, o_id, pin_id, p_id):
        product_dao = ProductDAO()
        people_dao = peopledao()
        p_priceperunit = product_dao.GetPricePerProductID(p_id)
        od_price = p_priceperunit * od_qty
        s_id = product_dao.getSupplierID_by_ProductID(p_id)
        ba_id = people_dao.getBankIDBy_SupplierID(s_id)

        od_id = people_dao.insert_product_to_OrderDetails(od_qty, od_price, o_id, pin_id, s_id, ba_id, p_id)

        #result = self.build_orderdetails_dict(od_id, od_qty, od_price, o_id, pin_id, s_id, ba_id, p_id)

        current_p_qty = product_dao.getPqty_by_PID(p_id)
        new_p_qty = current_p_qty - od_qty
        product_dao.update_product_quantity(p_id, new_p_qty)

        return od_id