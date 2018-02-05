from config.dbconfig import pg_config
import psycopg2


class peopledao:
    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['host'],
                                                                    pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    def filter_orders(self, args, int):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date, s_fname, s_lname " \
                "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
                "where orders.o_id = orderdetails.o_id "
        if int == 1:
            query = query + "AND o_id = %s;"
        elif int == 2:
            query = query + "AND o_date = %s;"
        elif int == 3:
            query = query + "AND c_id = %s;"
        elif int == 4:
            query = query + "AND od_qty = %s;"
        elif int == 5:
            query = query + "AND od_id = %s;"
        elif int == 6:
            query = query + "AND od_pprice = %s;"
        elif int == 7:
            query = query + "AND s_id = %s;"
        elif int == 8:
            query = query + "AND ba_id = %s;"
        elif int == 9:
            query = query + "AND p_id = %s;"
        else:
            query = query + "AND pin_id = %s;"
        cursor.execute(query, (args,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ################# USER ACCOUNTS ########################
    def getAccountByUsername(self, a_username):
        cursor = self.conn.cursor()
        query = "select * from account where a_username =%s;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    ################ ORDERS #####################

    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date, s_fname, s_lname " \
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
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode, country, district " \
                "from supplier natural inner join product natural inner join addresses " \
                "where supplier.saddress_id = addresses.address_id " \
                "AND p_id = %s;"
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

    def get_all_products_by_district(self):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, district " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "ORDER BY district;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_products_by_district_declared(self, district):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type, district " \
                "from addresses natural inner join supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "AND addresses.address_id = supplier.saddress_id " \
                "AND district = %s " \
                "ORDER BY district;"
        cursor.execute(query, (district,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def check_o_id(self, oid):
        cursor = self.conn.cursor()
        query = " select max(o_id) from orders;"
        cursor.execute(query)
        max_id = cursor.fetchone()[0]
        return 0 < oid <= max_id + 1

    def check_or_create_o_id(self, o_id, c_id, date):
        cursor = self.conn.cursor()
        query = " select max(o_id) from orders;"
        cursor.execute(query)
        max_id = cursor.fetchone()[0]
        if o_id <= max_id:
            return o_id
        else:
            query = "insert into orders(c_id, o_date) values (%s, %s) returning o_id;"
            cursor.execute(query, (c_id, date,))
            order_id = cursor.fetchone()[0]
            self.conn.commit()
            return order_id

    def check_pin(self, pin_id):
        cursor = self.conn.cursor()
        query = "select pin_fname, pin_lname from pin where pin_id = %s;"
        cursor.execute(query, (pin_id,))
        tuple = cursor.fetchone()
        print(tuple)
        if not tuple:
            return False
        else:
            query = "select c_id from creditcard where pin_id = %s;"
            cursor.execute(query, (pin_id,))
            c_id = cursor.fetchone()[0]
            tuple = tuple[0], tuple[1], c_id
            return tuple

    def check_sup(self, sup):
        cursor = self.conn.cursor()
        query = "select s_fname, s_lname from supplier where s_id = %s;"
        cursor.execute(query, (sup,))
        tuple = cursor.fetchone()
        if not tuple:
            return False
        else:
            query = "select ba_id from bankinfo where s_id = %s;"
            cursor.execute(query, (sup,))
            ba_id = cursor.fetchone()[0]
            tuple = tuple[0], tuple[1], ba_id
            return tuple

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

    def insert_new_admin(self, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone):
        cursor = self.conn.cursor()
        query = "insert into admins(ad_fname, ad_lname, ada_id, adaddress_id, ad_phone) values (%s, %s, %s, %s, " \
                "%s) returning ad_id;"
        cursor.execute(query, (ad_fname, ad_lname, ada_id, adaddress_id, ad_phone,))
        ad_id = cursor.fetchone()[0]
        self.conn.commit()
        return ad_id

    def update_admin(self, ad_id, ad_fname, ad_lname, ad_phone):
        cursor = self.conn.cursor()
        query = "update admins set ad_fname=%s, ad_lname=%s, ad_phone=%s where ad_id=%s returning ad_id;"
        cursor.execute(query, (ad_fname, ad_lname, ad_phone, ad_id,))
        ad_id = cursor.fetchone()[0]
        self.conn.commit()
        return ad_id

    def get_admin(self, ad_id):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city, zipcode," \
                " country, district " \
                "from admins natural inner join addresses " \
                "where addresses.address_id = admins.adaddress_id " \
                "AND ad_id = %s;"
        cursor.execute(query, (ad_id,))
        result = cursor.fetchone()
        return result

    #### ADDRESS #######################################################################################################
    def getAllAddress(self):
        cursor = self.conn.cursor()
        query = "select * from addresses;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByID(self, address_id):
        cursor = self.conn.cursor()
        query = "select * from addresses where address_id = %s;"
        result = []
        cursor.execute(query, (address_id,))
        for row in cursor:
            result.append(row)
        return result

    def insert_new_address(self, addressline1, city, country, district, zipcode):
        cursor = self.conn.cursor()
        query = "insert into addresses(addressline1, city, country, district, zipcode) values (%s, %s, %s, %s, %s) " \
                "returning address_id;"
        cursor.execute(query, (addressline1, city, country, district, zipcode,))
        address_id = cursor.fetchone()[0]
        self.conn.commit()
        return address_id

    def update_address(self, address_id, addressline1, city, country, district, zipcode):
        cursor = self.conn.cursor()
        query = "update addresses set addressline1 = %s, city = %s, country = %s, district = %s, zipcode = %s " \
                "where address_id = %s;"
        cursor.execute(query, (addressline1, city, country, district, zipcode, address_id,))
        self.conn.commit()
        return address_id

    ########### USER ###################################################################################################
    def insert_new_user(self, a_username, a_password):
        cursor = self.conn.cursor()
        query = "insert into account(a_username, a_password) values (%s, %s) returning a_id;"
        cursor.execute(query, (a_username, a_password,))
        a_id = cursor.fetchone()[0]
        self.conn.commit()
        return a_id

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

    def update_pin(self, pin_id, fname, lname, phone):
        cursor = self.conn.cursor()
        query = "update pin set pin_fname=%s, pin_lname=%s, pin_phone=%s where pin_id=%s returning pin_id;"
        cursor.execute(query, (fname, lname, phone, pin_id,))
        pin_id = cursor.fetchone()[0]
        self.conn.commit()
        return pin_id

    def get_pin(self, pin):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city, zipcode," \
                " country, district " \
                "from pin natural inner join addresses " \
                "where addresses.address_id = pin.pinaddress_id " \
                "AND pin_id = %s;"
        cursor.execute(query, (pin,))
        result = cursor.fetchone()
        return result

    ### S U P  ######################################################################################################
    def insert_new_sup(self, s_fname, s_lname, sa_id, saddress_id, s_phone):
        cursor = self.conn.cursor()
        query = "insert into supplier(s_fname, s_lname, sa_id, saddress_id, s_phone) values (%s, %s, %s, %s, " \
                "%s) returning s_id;"
        cursor.execute(query, (s_fname, s_lname, sa_id, saddress_id, s_phone), )
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id

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

    def get_sup(self, s_id):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, sa_id, saddress_id, s_phone, addressline1, city, zipcode," \
                " country, district " \
                "from supplier natural inner join addresses " \
                "where addresses.address_id = supplier.saddress_id " \
                "AND s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()
        return result

    def update_supplier(self, s_id, s_fname, s_lname, s_phone):
        cursor = self.conn.cursor()
        query = "update supplier set s_fname=%s, s_lname=%s, s_phone=%s where s_id=%s returning s_id;"
        cursor.execute(query, (s_fname, s_lname, s_phone, s_id,))
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id


    def view_bankinfo_by_SID(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from bankinfo where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()
        for row in cursor:
            result.append(row)
        return result


    def get_all_bank_info(self):
        cursor = self.conn.cursor()
        query = "select * from bankinfo;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def update_bankinfo(self, ba_id, s_id, ba_accnumber, ba_routingnumber):
        cursor = self.conn.cursor()
        query = "update bankinfo set s_id = %s, ba_accnumber = %s, ba_rountingnumber = %s where ba_id = %s;"
        cursor.execute(query, (s_id, ba_accnumber, ba_routingnumber, ba_id,))
        self.conn.commit()
        return ba_id


    def insert_bankinfo(self, s_id, ba_accnumber, ba_routingnumber):
        cursor = self.conn.cursor()
        query = "insert into bankinfo(s_id, ba_accnumber, ba_rountingnumber) values (%s, %s, %s) returning ba_id;"
        cursor.execute(query, (s_id, ba_accnumber, ba_routingnumber,))
        ba_id = cursor.fetchone()[0]
        self.conn.commit()
        return ba_id


    def view_creditcard_by_PIN(self, pin_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard where pin_id = %s;"
        cursor.execute(query, (pin_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def view_creditcard(self):
        cursor = self.conn.cursor()
        query = "select * from creditcard;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result



    def get_bankaccount_by_s_id(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from bankinfo where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def search_account_by_a_id(self, a_id):
        cursor = self.conn.cursor()
        query = "select * from account where a_id = %s;"
        cursor.execute(query, (a_id,))
        result = cursor.fetchone()
        return result


    def get_creditcard(self, c_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard where c_id = %s;"
        cursor.execute(query, (c_id,))
        result = cursor.fetchone()
        return result


    def check_bankinfo(self, s_id):
        cursor = self.conn.cursor()
        query = "select ba_id from bankinfo where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()[0]
        return result


    def get_all_accounts(self):
        cursor = self.conn.cursor()
        query = "select * from account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def update_creditcard(self, c_id, c_cardtype, c_cardnumber, c_cardname, pin_id, address_id):
        cursor = self.conn.cursor()
        query = "update creditcard set c_cardtype = %s, c_cardnumber = %s, c_cardname = %s, pin_id = %s, " \
                "address_id = %s  where c_id = %s;"
        cursor.execute(query, (c_cardtype, c_cardnumber, c_cardname, pin_id, address_id, c_id,))
        self.conn.commit()
        return c_id


    def insert_creditcard(self, c_cardtype, c_cardname, pin_id, address_id, c_cardnumber):
        cursor = self.conn.cursor()
        query = "insert into creditcard(c_cardtype, c_cardname, pin_id, address_id, c_cardnumber) values " \
                "(%s, %s, %s, %s, %s) returning c_id;"
        cursor.execute(query, (c_cardtype, c_cardname, pin_id, address_id, c_cardnumber,))
        c_id = cursor.fetchone()[0]
        self.conn.commit()
        return c_id
