from config.dbconfig import pg_config
import psycopg2


class peopledao:
    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['host'],
                                                                    pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)



    def getAccountByUsername(self, a_username):
        cursor = self.conn.cursor()
        query = "select * from account where a_username =%s;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result



    '''Return all order info'''

    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier;"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''encontrar productos por supplidor (id) '''

    def getProductsBySupplierId(self, s_id):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type " \
                "from supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND s_id = %s " \
                "ORDER BY p_name;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''encontrar productos por supplidor (primernombre) '''

    def getProductsBySupplierName(self, s_fname):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type " \
                "from supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND s_fname = %s " \
                "ORDER BY p_name;"
        cursor.execute(query, (s_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''encontrar productos por supplidor (nombre completo)'''

    def getProductsBySupplierFullName(self, s_fname, s_lname):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type " \
            "from supplier natural inner join product natural inner join category " \
            "where supplier.s_id = product.s_id " \
            "AND product.ct_id = category.ct_id " \
            "AND s_fname = %s " \
            "AND s_lname = %s " \
            "ORDER BY p_name;"
        cursor.execute(query, (s_fname, s_lname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''encontrar supplidor por producto (id) '''

    def getSupplierByProductId(self, p_id):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone from supplier natural inner join product where p_id = %s;"
        cursor.execute(query, (p_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''encontrar supplidor por producto (nombre producto) '''

    def getSupplierByProductName(self, p_name):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone from supplier natural inner join product where p_name = %s;"
        cursor.execute(query, (p_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''helper for handler'''

    def getSupplierById(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()
        return result

    '''Encontrar todas las ordenes de una Persona'''

    def getOrdersByPersonInNeedById(self, pin_id):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
                "where pin.pin_id = %s;"
        cursor.execute(query, (pin_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''Encontrar todas las ordenes de una Persona'''

    def getOrdersByPersonInNeedByFirstName(self, pin_fname):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
                "where pin.pin_fname = %s;"
        cursor.execute(query, (pin_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''Encontrar todas las ordenes de una Persona'''

    def getOrdersByPersonInNeedByFullName(self, pin_fname, pin_lname):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
                "where pin.pin_fname = %s and pin.pin_lname = %s;"
        cursor.execute(query, (pin_fname, pin_lname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''Encontrar todas las ordenes de un suplidor'''

    def getOrdersBySupplierById(self, s_id):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
                "where supplier.s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''Encontrar todas las ordenes de un suplidor'''

    def getOrdersBySuppplierByFirstName(self, s_fname):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
                "where supplier.s_fname = %s;"

        cursor.execute(query, (s_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''Encontrar todas las ordenes de un suplidor'''

    def getOrdersBySupplierByFullName(self, s_fname, s_lname):

        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
                "where supplier.s_fname = %s and supplier.s_lname = %s;"
        cursor.execute(query, (s_fname, s_lname))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def get_all_products_by_supplier(self):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type " \
                "from supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "ORDER BY p_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_products_by_city(self):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, city " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "ORDER BY city;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_products_by_city_declared(self, city):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, city " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "AND city = %s " \
                "ORDER BY city;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_products_by_zipcode(self):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, zipcode " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "ORDER BY zipcode;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_products_by_zipcode_declared(self, zipcode):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, zipcode " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "AND zipcode = %s " \
                "ORDER BY zipcode;"
        cursor.execute(query, (zipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_products_by_country(self):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, country " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "ORDER BY country;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_products_by_country_declared(self, country):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, country " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "AND country = %s " \
                "ORDER BY country;"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    ### A D M I N I S T R A T O R S ####################################################################################
    def getAllAdmin(self):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByID(self, ad_id):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id and ad_id = %s;"
        cursor.execute(query, (ad_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByFNAME(self, ad_fname):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id and ad_fname = %s;"
        cursor.execute(query, (ad_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByPHONE(self, ad_phone):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id and ad_phone = %s;"
        cursor.execute(query, (ad_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByCITY(self, city):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id and city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByCOUNTRY(self, country):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id and country = %s;"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByDISTRICT(self, district):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id and district = %s;"
        cursor.execute(query, (district,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GeADMINByFULLNAME(self, ad_fname, ad_lname):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id and ad_fname = %s and ad_lname = %s;"
        cursor.execute(query, (ad_fname, ad_lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_new_address(self, addressline1, city, country, district, zipcode):
        cursor = self.conn.cursor()
        query = "insert into addresses(addressline1, city, country, district, zipcode) values (%s, %s, %s, %s, %s) " \
                "returning address_id;"
        cursor.execute(query, (addressline1, city, zipcode, country, district,))
        address_id = cursor.fetchone()[0]
        self.conn.commit()
        return address_id

    def insert_new_user(self, a_username, a_password):
        cursor = self.conn.cursor()
        query = "insert into account(a_username, a_password) values (%s, %s) returning a_id;"
        cursor.execute(query, (a_username, a_password,))
        a_id = cursor.fetchone()[0]
        self.conn.commit()
        return a_id

    def insert_new_admin(self, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone):
        cursor = self.conn.cursor()
        query = "insert into admins(ad_fname, ad_lname, ada_id, adaddress_id, ad_phone) values (%s, %s, %s, %s, " \
                "%s) returning ad_id;"
        cursor.execute(query, (ad_fname, ad_lname, ada_id, adaddress_id, ad_phone,))
        ad_id = cursor.fetchone()[0]
        self.conn.commit()
        return ad_id

    ### P I N ######################################################################################################
    def getAllpin(self):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                "zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetPINByID(self, pin_id):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id and pin_id = %s;"
        cursor.execute(query, (pin_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetPINByFNAME(self, pin_fname):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id and pin_fname = %s;"
        cursor.execute(query, (pin_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetPINByPHONE(self, pin_phone):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id and pin_phone = %s;"
        cursor.execute(query, (pin_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetPINByCITY(self, city):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id and city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetPINByCOUNTRY(self, country):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id and country = %s;"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetPINByDISTRICT(self, district):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id and district = %s;"
        cursor.execute(query, (district,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetPINByFULLNAME(self, pin_fname, pin_lname):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id and pin_fname = %s and pin_lname = %s;"
        cursor.execute(query, (pin_fname, pin_lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_new_pin(self, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone):
        cursor = self.conn.cursor()
        query = "insert into pin(pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone) values (%s, %s, %s, %s, " \
                "%s) returning pin_id;"
        cursor.execute(query, (pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone,))
        pin_id = cursor.fetchone()[0]
        self.conn.commit()
        return pin_id

    ### P I N ######################################################################################################
    def getAllSUP(self):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetSUPByID(self, s_id):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id and s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetSUPByFNAME(self, s_fname):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id and s_fname = %s;"
        cursor.execute(query, (s_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetSUPByPHONE(self, s_phone):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id and s_phone = %s;"
        cursor.execute(query, (s_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetSUPByCITY(self, city):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id and city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetSUPByCOUNTRY(self, country):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id and country = %s;"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetSUPByDISTRICT(self, district):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id and district = %s;"
        cursor.execute(query, (district,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetSUPByFULLNAME(self, s_fname, s_lname):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id and s_fname = %s and s_lname = %s;"
        cursor.execute(query, (s_fname, s_lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ''' not specified in phase 2 specs'''
    '''def getRequestsbypersoninneed(self, pin_id):
        cursor = self.conn.cursor()
        query = "select R_id, R_pname, R_qty, R_date, pin_id, pin_fname, pin_lname from Request natural inner join pin where pin_id = %s;"
        cursor.execute(query, (pin_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getbankacccountbysupplierid(self, s_id):
            cursor = self.conn.cursor()
            query = "select * from bankinfo where s_id = %s;"
            cursor.execute(query, (s_id,))
            result = cursor.fetchone()
            return result
    def getcreditcardinformationbypersoninneedid(self, pin_id):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, c_id, c_cardtype, c_cardnumber, c_cardname, from pin natural inner join creditcard natural inner join ownscreditcard where pin_id = %s;"
        cursor.execute(query, (pin_id,))
        for row in cursor:
            result.append(row)
        return result
    def getsuppliersbycity(self, city):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, s_phone from supplier natural inner join addresses where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getpersoninneedbycity(self, city):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pin_phone from pin natural inner join addresses where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getpersoninneedbyid(self, pin_id):
            cursor = self.conn.cursor()
            query = "select * from pin where pin_id = %s;"
            cursor.execute(query, (pin_id,))
            result = cursor.fetchone()
            return result'''