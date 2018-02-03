from flask import jsonify
from dao.people import peopledao


class peopleHandler:
    def build_admin_dict(self, row):
        result = {}
        result['ad_id'] = row[0]
        result['ad_fname'] = row[1]
        result['ad_lname'] = row[2]
        result['ada_id'] = row[3]
        result['adaddress_id'] = row[4]
        result['ad_phone'] = row[5]
        result['addressline1'] = row[6]
        result['city'] = row[7]
        result['zipcode'] = row[8]
        result['country'] = row[9]
        result['district'] = row[10]
        return result

    def build_address_dict(self, row):
        result = ()
        result['address_id'] = row[1]
        result['addressline1'] = row[2]
        result['city'] = row[3]
        result['zipcode'] = row[4]
        result['country'] = row[5]
        result['district'] = row[6]
        return result

    def build_adminSOLO_dict(self, row):
        result = {}
        result['ad_id'] = row[0]
        result['ad_fname'] = row[1]
        result['ad_lname'] = row[2]
        result['ada_id'] = row[3]
        result['adaddress_id'] = row[4]
        result['ad_phone'] = row[5]
        return result


    def build_adminINS_dict(self, ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode, country, district):
        result = {}
        result['ad_id'] = ad_id
        result['ad_fname'] = ad_fname
        result['ad_lname'] = ad_lname
        result['ada_id'] = ada_id
        result['adaddress_id'] = adaddress_id
        result['ad_phone'] = ad_phone
        result['addressline1'] = addressline1
        result['city'] = city
        result['zipcode'] = zipcode
        result['country'] = country
        result['district'] = district
        return result

    def build_pin_dict(self, row):
        result = {}
        result['pin_id'] = row[0]
        result['pin_fname'] = row[1]
        result['pin_lname'] = row[2]
        result['pina_id'] = row[3]
        result['pinaddress_id'] = row[4]
        result['pin_phone'] = row[5]
        result['addressline1'] = row[6]
        result['city'] = row[7]
        result['zipcode'] = row[8]
        result['country'] = row[9]
        result['district'] = row[10]
        return result

    def build_pinSOLO_dict(self, row):
        result = {}
        result['pin_id'] = row[0]
        result['pin_fname'] = row[1]
        result['pin_lname'] = row[2]
        result['pina_id'] = row[3]
        result['pinaddress_id'] = row[4]
        result['pin_phone'] = row[5]
        return result

    def build_pinINS_dict(self, pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode, country, district):
        result = {}
        result['pin_id'] = pin_id
        result['pin_fname'] = pin_fname
        result['pin_lname'] = pin_lname
        result['pina_id'] = pina_id
        result['pinaddress_id'] = pinaddress_id
        result['pin_phone'] = pin_phone
        result['addressline1'] = addressline1
        result['city'] = city
        result['zipcode'] = zipcode
        result['country'] = country
        result['district'] = district
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['s_fname'] = row[1]
        result['s_lname'] = row[2]
        result['sa_id'] = row[3]
        result['adressid'] = row[4]
        result['s_phone'] = row[5]
        result['addressline1'] = row[6]
        result['city'] = row[7]
        result['zipcode'] = row[8]
        result['country'] = row[9]
        result['district'] = row[10]
        return result

    def build_subSOLO_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['s_fname'] = row[1]
        result['s_lname'] = row[2]
        result['sa_id'] = row[3]
        result['aaddress_id'] = row[4]
        result['s_phone'] = row[5]
        return result

    def build_supplierINS_dict(self, s_id, s_fname, s_lname, sa_id, adressid, s_phone, addressline1, city, zipcode, country, district):
        result = {}
        result['s_id'] = s_id
        result['s_fname'] = s_fname
        result['s_lname'] = s_lname
        result['sa_id'] = sa_id
        result['adressid'] = adressid
        result['s_phone'] = s_phone
        result['addressline1'] = addressline1
        result['city'] = city
        result['zipcode'] = zipcode
        result['country'] = country
        result['district'] = district
        return result

    def build_product_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['ct_id'] = row[1]
        result['s_id'] = row[2]
        result['p_name'] = row[3]
        result['p_qty'] = row[4]
        result['p_unit'] = row[5]
        result['p_priceperunit'] = row[6]
        return result

    def build_new_product(self, row):
        result = {}
        result['p_id'] = row[0]
        result['ct_id'] = row[1]
        result['s_id'] = row[2]
        result['p_name'] = row[3]
        result['p_qty'] = row[4]
        result['p_unit'] = row[5]
        result['p_priceperunit'] = row[6]
        result['s_fname'] = row[7]
        result['s_lname'] = row[8]
        result['ct_type'] = row[9]
        return result

    def build_new_product_declared(self, row, input):
        result = {}
        result['p_id'] = row[0]
        result['ct_id'] = row[1]
        result['s_id'] = row[2]
        result['p_name'] = row[3]
        result['p_qty'] = row[4]
        result['p_unit'] = row[5]
        result['p_priceperunit'] = row[6]
        result['s_fname'] = row[7]
        result['s_lname'] = row[8]
        result['ct_type'] = row[9]
        result[input] = row[10]
        return result

    def build_orderinfo_dict(self, row):
        result = {}
        result['o_id'] = row[0]
        result['od_id'] = row[1]
        result['od_qty'] = row[2]
        result['od_pprice'] = row[3]
        result['s_id'] = row[4]
        result['ba_id'] = row[5]
        result['p_id'] = row[6]
        result['p_name'] = row[7]
        result['pin_id'] = row[8]
        result['pin_fname'] = row[9]
        result['pin_lname'] = row[10]
        result['c_id'] = row[11]
        result['o_date'] = row[12]
        return result

    '''return everyone registered as person in need'''

    def getAllPeopleInNeed(self):
        dao = peopledao()
        pin_list = dao.getAllPeopleInNeed()
        result_list = []
        for row in pin_list:
            result = self.build_pin_dict(row)
            result_list.append(result)
        return jsonify(PeopleInNeed=result_list)

    '''return everyone registered as supplier'''

    def getAllSuppliers(self):
        dao = peopledao()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    '''return everyone registered as administrator'''

    def getAllAdminstrators(self):
        dao = peopledao()
        suppliers_list = dao.getAllAdmin()
        result_list = []
        for row in suppliers_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    '''Get All Orders'''

    def getAllOrders(self):
        dao = peopledao()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    '''encontrar productos por supplidor '''

    def getProductsBySupplier(self, args):
        s_id = args.get("s_id")
        s_fname = args.get("s_fname")
        s_lname = args.get("s_lname")
        dao = peopledao()
        product_list = []
        if (len(args) == 2) and s_fname and s_lname:
            product_list = dao.getProductsBySupplierFullName(s_fname, s_lname)
        elif (len(args) == 1) and s_fname:
            product_list = dao.getProductsBySupplierName(s_fname)
        elif (len(args) == 1) and s_id:
            product_list = dao.getProductsBySupplierId(s_id)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_new_product(row)
            result_list.append(result)
        return jsonify(ProductsBySupplier=result_list)

    '''encontrar supplidor por producto'''

    def getSupplierByProduct(self, args):
        p_id = args.get("p_id")
        p_name = args.get("p_name")
        dao = peopledao()
        product_list = []
        if (len(args) == 1) and p_id:
            product_list = dao.getSupplierByProductId(p_id)
        elif (len(args) == 1) and p_name:
            product_list = dao.getSupplierByProductName(p_name)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SupplierByProduct=result_list)

    '''Encontrar las ordenes de una persona'''

    def getOrdersByPersonInNeed(self, args):
        pin_id = args.get("pin_id")
        pin_fname = args.get("pin_fname")
        pin_lname = args.get("pin_lname")
        dao = peopledao()
        order_list = []
        if (len(args) == 1) and pin_id:
            order_list = dao.getOrdersByPersonInNeedById(pin_id)
        elif (len(args) == 1) and pin_fname:
            order_list = dao.getOrdersByPersonInNeedByFirstName(pin_fname)
        elif (len(args) == 2) and pin_fname and pin_lname:
            order_list = dao.getOrdersByPersonInNeedByFullName(pin_fname, pin_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in order_list:
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return jsonify(OrdersByPersonInNeed=result_list)

    '''Encontrar las ordenes de una supplier'''

    def getOrdersBySupplier(self, args):
        s_id = args.get("s_id")
        s_fname = args.get("s_fname")
        s_lname = args.get("s_lname")
        dao = peopledao()
        order_list = []
        if (len(args) == 1) and s_id:
            order_list = dao.getOrdersBySupplierById(s_id)
        elif (len(args) == 1) and s_fname:
            order_list = dao.getOrdersBySuppplierByFirstName(s_fname)
        elif (len(args) == 2) and s_fname and s_lname:
            order_list = dao.getOrdersBySupplierByFullName(s_fname, s_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in order_list:
            print(row)
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return jsonify(OrdersBySupplier=result_list)

    def get_all_products_by_supplier(self):
        dao = peopledao()
        product_list = dao.get_all_products_by_supplier()
        result_list = []
        for row in product_list:
            result = self.build_new_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    def get_all_products_by_city(self, args):
        dao = peopledao()
        city = args.get('city')
        if not city:
            product_list = dao.get_all_products_by_city()
        else:
            product_list = dao.get_all_products_by_city_declared(city)
        result_list = []
        for row in product_list:
            result = self.build_new_product_declared(row, 'city')
            result_list.append(result)
        return jsonify(Product=result_list)

    def get_all_products_by_zipcode(self, args):
        dao = peopledao()
        zipcode= args.get('zipcode')
        if not zipcode:
            product_list = dao.get_all_products_by_zipcode()
        else:
            product_list = dao.get_all_products_by_zipcode_declared(zipcode)
        result_list = []
        for row in product_list:
            result = self.build_new_product_declared(row, 'zipcode')
            result_list.append(result)
        return jsonify(Product=result_list)

    def get_all_products_by_country(self, args):
        dao = peopledao()
        country = args.get('country')
        if not country:
            product_list = dao.get_all_products_by_country()
        else:
            product_list = dao.get_all_products_by_country_declared(country)
        result_list = []
        for row in product_list:
            result = self.build_new_product_declared(row, 'country')
            result_list.append(result)
        return jsonify(Product=result_list)

    def getAllAddress(self):
        dao = peopledao()
        sup_list = dao.getAllAddress()
        result_list = []
        for row in sup_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Address=result_list)

    ##SEARCH SUP BY REQUESTS##
    def getAddressByID(self, args):
        address_id = args.get("address_id")
        dao = peopledao()
        request_list = []

        if (len(args) == 1) and address_id:
            request_list = dao.getAddressByID(address_id)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(AdressByID=result_list)

    def updateAddresses(self, addresses_id, form):
        dao = peopledao()
        if not dao.getAddressByID(addresses_id):
            return jsonify(Error="Request not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                addressline1 = form['addressline1']
                city = form['city']
                country = form['country']
                district = form['district']
                zipcode = form['zipcode']
                if addresses_id and addressline1 and city and country and district and zipcode:
                    dao.update_address(addresses_id, addressline1, city, country, district, zipcode)
                    result = self.build_address_dict(addresses_id, addressline1, city, country, district, zipcode)
                    return jsonify(UpdatedRequest=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    ########## A D M I N ###############################################################################################

    def updateAdmin(self, ad_id, form):
        dao = peopledao()
        if not dao.GetADMINByID(ad_id):
            return jsonify(Error="Request not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                ad_fname = form['ad_fname']
                ad_lname = form['ad_lname']
                ada_id = form['ada_id']
                adaddress_id = form['adaddress_id']
                ad_phone = form['ad_phone']
                if ad_fname and ad_lname and ada_id and adaddress_id and ad_phone:
                    dao.update_admin(ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone)
                    result = self.build_adminSOLO_dict(ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone)
                    return jsonify(UpdatedRequest=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def insert_admin(self, form):
        if len(form) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            ad_fname = form['ad_fname']
            ad_lname = form['ad_lname']
            a_username = form['a_username']
            a_password = form['a_password']
            ad_phone = form['ad_phone']
            addressline1 = form['addressline1']
            city = form['city']
            zipcode = form['zipcode']
            country = form['country']
            district = form['district']
            if ad_fname and ad_lname and ad_phone and addressline1 and city and zipcode and country \
                    and district and a_username and a_password:
                dao = peopledao()
                adaddress_id = dao.insert_new_address(addressline1, city, zipcode, country, district)
                ada_id = dao.insert_new_user(a_username, a_password)
                ad_id = dao.insert_new_admin(ad_fname, ad_lname, ada_id, adaddress_id, ad_phone)
                result = self.build_adminINS_dict(ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone,
                                                  addressline1, city, zipcode, country, district)
                return jsonify(NewAdministrator=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllAdmin(self):
        dao = peopledao()
        admin_list = dao.getAllAdmin()
        result_list = []
        for row in admin_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    ##SEARCH ADMIN BY REQUESTS##
    def searchADMINByRequests(self, args):
        ad_id = args.get("ad_id")
        ad_fname = args.get("ad_fname")
        ad_lname = args.get("ad_lname")
        ad_phone = args.get("ad_phone")
        city = args.get("city")
        country = args.get("country")
        district = args.get("district")
        dao = peopledao()
        request_list = []

        if (len(args) == 1) and ad_id:
            request_list = dao.GetADMINByID(ad_id)
        elif (len(args) == 1) and ad_fname:
            request_list = dao.GetADMINByFNAME(ad_fname)
        elif (len(args) == 1) and ad_phone:
            request_list = dao.GetADMINByPHONE(ad_phone)
        elif (len(args) == 1) and city:
            request_list = dao.GetADMINByCITY(city)
        elif (len(args) == 1) and country:
            request_list = dao.GetADMINByCOUNTRY(country)
        elif (len(args) == 1) and district:
            request_list = dao.GetADMINByDISTRICT(district)
        elif (len(args) == 2) and ad_fname and ad_lname:
            request_list = dao.GeADMINByFULLNAME(ad_fname, ad_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
            print(row)

        return jsonify(Request=result_list)

    ####### P E O P L E  I N  N E E D ##################################################################################

    def insert_pin(self, form):
        if len(form) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            pin_fname = form['pin_fname']
            pin_lname = form['pin_lname']
            a_username = form['a_username']
            a_password = form['a_password']
            pin_phone = form['pin_phone']
            addressline1 = form['addressline1']
            city = form['city']
            zipcode = form['zipcode']
            country = form['country']
            district = form['district']
            if pin_fname and pin_lname and pin_phone and addressline1 and city and zipcode and country \
                    and district and a_username and a_password:
                dao = peopledao()
                pinaddress_id = dao.insert_new_address(addressline1, city, zipcode, country, district)
                pina_id = dao.insert_new_user(a_username, a_password)
                pin_id = dao.insert_new_pin(pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone)
                result = self.build_adminINS_dict(pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone,
                                                  addressline1, city, zipcode, country, district)
                return jsonify(NewPersonInNeed=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllpin(self):
        dao = peopledao()
        pin_list = dao.getAllpin()
        result_list = []
        for row in pin_list:
            result = self.build_pin_dict(row)
            result_list.append(result)
        return jsonify(PIN=result_list)

    ##SEARCH PIN BY REQUESTS##
    def searchPINByRequests(self, args):
        pin_id = args.get("pin_id")
        pin_fname = args.get("pin_fname")
        pin_lname = args.get("pin_lname")
        pin_phone = args.get("pin_phone")
        city = args.get("city")
        country = args.get("country")
        district = args.get("district")
        dao = peopledao()
        request_list = []

        if (len(args) == 1) and pin_id:
            request_list = dao.GetPINByID(pin_id)
        elif (len(args) == 1) and pin_fname:
            request_list = dao.GetPINByFNAME(pin_fname)
        elif (len(args) == 1) and pin_phone:
            request_list = dao.GetPINByPHONE(pin_phone)
        elif (len(args) == 1) and city:
            request_list = dao.GetPINByCITY(city)
        elif (len(args) == 1) and country:
            request_list = dao.GetPINByCOUNTRY(country)
        elif (len(args) == 1) and district:
            request_list = dao.GetPINByDISTRICT(district)
        elif (len(args) == 2) and pin_fname and pin_lname:
            request_list = dao.GetPINByFULLNAME(pin_fname, pin_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
            print(row)

        return jsonify(Request=result_list)
    ####################################################################################################################
    ####### S U P P L I E R ############################################################################################

    def insert_sup(self, form):
        if len(form) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            s_fname = form['s_fname']
            s_lname = form['s_lname']
            a_username = form['a_username']
            a_password = form['a_password']
            s_phone = form['s_phone']
            addressline1 = form['addressline1']
            city = form['city']
            zipcode = form['zipcode']
            country = form['country']
            district = form['district']
            if s_fname and s_lname and s_phone and addressline1 and city and zipcode and country \
                    and district and a_username and a_password:
                dao = peopledao()
                saddress_id = dao.insert_new_address(addressline1, city, zipcode, country, district)
                sa_id = dao.insert_new_user(a_username, a_password)
                s_id = dao.insert_new_sup(s_fname, s_lname, sa_id, saddress_id, s_phone)
                result = self.build_supplierINS_dict(s_id, s_fname, s_lname, sa_id, saddress_id, s_phone,
                                                  addressline1, city, zipcode, country, district)
                return jsonify(NewSupplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def getAllsup(self):
        dao = peopledao()
        sup_list = dao.getAllSUP()
        result_list = []
        for row in sup_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(PIN=result_list)

    ##SEARCH SUP BY REQUESTS##
    def searchSUPByRequests(self, args):
        s_id = args.get("s_id")
        s_fname = args.get("s_fname")
        s_lname = args.get("s_lname")
        s_phone = args.get("s_phone")
        city = args.get("city")
        country = args.get("country")
        district = args.get("district")
        dao = peopledao()
        request_list = []

        if (len(args) == 1) and s_id:
            request_list = dao.GetSUPByID(s_id)
        elif (len(args) == 1) and s_fname:
            request_list = dao.GetSUPByFNAME(s_fname)
        elif (len(args) == 1) and s_phone:
            request_list = dao.GetSUPByPHONE(s_phone)
        elif (len(args) == 1) and city:
            request_list = dao.GetSUPByCITY(city)
        elif (len(args) == 1) and country:
            request_list = dao.GetSUPByCOUNTRY(country)
        elif (len(args) == 1) and district:
            request_list = dao.GetSUPByDISTRICT(district)
        elif (len(args) == 2) and s_fname and s_lname:
            request_list = dao.GetSUPByFULLNAME(s_fname, s_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
            print(row)

        return jsonify(Request=result_list)