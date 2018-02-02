from config.dbconfig import pg_config
import psycopg2


class peopledao:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['host'],
                                                                    pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    '''Return everyone registered as person in need'''
    def getAllPeopleInNeed(self):
        cursor = self.conn.cursor()
        query = "select pin_id, pin_fname, pin_lname, a_id, pin_phone, addressid, addressline1, city, zipcode, country, district " \
                "from pin natural inner join addresses;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select s_id, s_fname, s_lname, a_id, s_phone, addressid, addressline1, city, zipcode, country, district " \
                "from supplier natural inner join addresses;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    ### A D M I N I S T R A T O R S ####################################################################################
    def getAllAdmin(self):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByID(self, ad_id):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses" \
                "where ad_id = %s;"
        cursor.execute(query, (ad_id,))
        result = cursor.fetchone()
        return result

    def GetADMINByFNAME(self, ad_fname):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses" \
                "where ad_fname = %s;"
        cursor.execute(query, (ad_fname,))
        result = cursor.fetchone()
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByPHONE(self, ad_phone):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses" \
                "where ad_phone = %s;"
        cursor.execute(query, (ad_phone,))
        result = cursor.fetchone()
        return result

    def GetADMINByCITY(self, city):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses" \
                "where city = %s;"
        cursor.execute(query, (city,))
        result = cursor.fetchone()
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByCOUNTRY(self, country):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses" \
                "where country = %s;"
        cursor.execute(query, (country,))
        result = cursor.fetchone()
        for row in cursor:
            result.append(row)
        return result

    def GetADMINByDISTRICT(self, district):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses" \
                "where district = %s;"
        cursor.execute(query, (district,))
        result = cursor.fetchone()
        for row in cursor:
            result.append(row)
        return result

    def GeADMINByFULLNAME(self, ad_fname, ad_lname):
        cursor = self.conn.cursor()
        query = "select ad_id, ad_fname, ad_lname, a_id, ad_phone, addressid, addressline1, city, zipcode, country, district " \
                "from admin natural inner join addresses" \
                "where ad_fname = %s and ad_lname = %s;"
        cursor.execute(query, (ad_fname, ad_lname,))
        result = cursor.fetchone()
        for row in cursor:
            result.append(row)
        return result
    ####################################################################################################################


    '''helper for handler'''

    def getSupplierById(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()
        return result

    '''encontrar productos por supplidor (id) '''
    def getProductsBySupplierId(self, s_id):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit from product where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''encontrar productos por supplidor (primernombre) '''
    def getProductsBySupplierName(self, s_fname):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit from suppliers natural inner join product s_fname = %s;"
        cursor.execute(query, (s_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''encontrar productos por supplidor (nombre completo)'''

    def getProductsBySupplierFullName(self, s_fname, s_lname):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit from supplier natural inner join product where s_fname = %s and s_lname = %s;"
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



    def create_address(self, address, city, country, district, zipcode):
        cursor = self.conn.cursor()
        query = "insert into addresses(addressline1, city, country, district, zipcode)values(%s, %s, %s, %s, %s);"
        cursor.execute(query, (address, city, country, district, zipcode,))
        self.conn.commit()
        query = "select address_id from addresses where addressline1= %s AND city= %s AND country= %s " \
                "AND district = %s AND zipcode = %s;"
        cursor.execute(query, (address, city, country, district, zipcode,))
        result = cursor.fetchone()
        self.conn.commit()
        if not result[0] == None:
            return result[0]
        return None

    def create_supplier(self, fname, lname, phone, ac_id, address_id):
        cursor = self.conn.cursor()
        query = "INSERT INTO supplier(s_fname, s_lname, sa_id, saddress_id, s_phone)VALUES(%s, %s, %s, %s, %s);"
        cursor.execute(query,(fname, lname, ac_id, address_id, phone,))
        self.conn.commit()
        query = "select max(s_id) from supplier where s_phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        self.conn.commit()
        if not result[0] == None:
            return result[0]
        return None

    def create_pin(self, fname, lname, phone, ac_id, address_id):
        cursor = self.conn.cursor()
        query = "INSERT INTO pin(pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone)VALUES(%s, %s, %s, %s, %s);"
        cursor.execute(query,(fname, lname, ac_id, address_id, phone,))
        self.conn.commit()
        query = "select max(pin_id) from pin where pin_phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        self.conn.commit()
        if not result[0] == None:
            return result[0]
        return None

    def insert_new_cc(self, c_cardtype, c_cardname, pin_id, address_id, c_cardnumber):
        cursor = self.conn.cursor()
        query = "insert into creditcard(c_cardtype, c_cardname, pin_id, address_id, c_cardnumber) values (%s, %s, %s, %s, %s) returning c_id;"
        cursor.execute(query, (c_cardtype, c_cardname, pin_id, address_id, c_cardnumber,))
        c_id = cursor.fetchone()[0]
        self.conn.commit()
        return c_id

    def getCreditCardByPinID(self, pin_id):

        cursor = self.conn.cursor()
        query = "Select * " \
                "from creditcard " \
                "where creditcard.pin_id = %s ;"
        cursor.execute(query, (pin_id,))
        result = cursor.fetchone()
        return result

    def update_cc(self, c_id, c_cardtype, c_cardname, pin_id, address_id, c_cardnumber):
        cursor = self.conn.cursor()
        query = "update creditcard set c_cardtype = %s, c_cardname = %s, pin_id = %s, address_id = %s, c_cardnumber = %s where c_id = %s;"
        cursor.execute(query, (c_cardtype, c_cardname, pin_id, address_id, c_cardnumber, c_id,))
        self.conn.commit()
        return c_id

    def getCreditCardByPinIDandC_ID(self, pin_id):
        cursor = self.conn.cursor()
        query = "Select * " \
                "from creditcard " \
                "where creditcard.pin_id = %s;"
        cursor.execute(query, (pin_id,))
        result = cursor.fetchone()
        return result



    def getBankIDBy_SupplierID(self, s_id):
        cursor = self.conn.cursor()
        query = "Select ba_id " \
                "from bankinfo "\
                "where s_id = %s ;"
        cursor.execute(query, (s_id,))
        ba_id = cursor.fetchone()[0]
        return ba_id


#### U N U S E D  O R  O B S O L E T E ####
    # def getPINByFirstName(self, pin_fname):
    #     cursor = self.conn.cursor()
    #     query = "select * from pin where pin_fname = %s;"
    #     cursor.execute(query, (pin_fname,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # ''' not specified in phase 2 specs'''
    # '''def getRequestsbypersoninneed(self, pin_id):
    #     cursor = self.conn.cursor()
    #     query = "select R_id, R_pname, R_qty, R_date, pin_id, pin_fname, pin_lname from Request natural inner join pin where pin_id = %s;"
    #     cursor.execute(query, (pin_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def getbankacccountbysupplierid(self, s_id):
    #         cursor = self.conn.cursor()
    #         query = "select * from bankinfo where s_id = %s;"
    #         cursor.execute(query, (s_id,))
    #         result = cursor.fetchone()
    #         return result
    #
    # def getcreditcardinformationbypersoninneedid(self, pin_id):
    #     cursor = self.conn.cursor()
    #     query = "select pin_id, pin_fname, pin_lname, c_id, c_cardtype, c_cardnumber, c_cardname, from pin natural inner join creditcard natural inner join ownscreditcard where pin_id = %s;"
    #     cursor.execute(query, (pin_id,))
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def getsuppliersbycity(self, city):
    #     cursor = self.conn.cursor()
    #     query = "select s_id, s_fname, s_lname, s_phone from supplier natural inner join addresses where city = %s;"
    #     cursor.execute(query, (city,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def getpersoninneedbycity(self, city):
    #     cursor = self.conn.cursor()
    #     query = "select pin_id, pin_fname, pin_lname, pin_phone from pin natural inner join addresses where city = %s;"
    #     cursor.execute(query, (city,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def getpersoninneedbyid(self, pin_id):
    #         cursor = self.conn.cursor()
    #         query = "select * from pin where pin_id = %s;"
    #         cursor.execute(query, (pin_id,))
    #         result = cursor.fetchone()
    #         return result'''
    #
    # '''Encontrar todas las ordenes de una Persona'''
    #
    # def getOrdersByPersonInNeedById(self, pin_id):
    #     cursor = self.conn.cursor()
    #     query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
    #             "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
    #             "where pin.pin_id = %s;"
    #     cursor.execute(query, (pin_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # '''Encontrar todas las ordenes de una Persona'''
    #
    # def getOrdersByPersonInNeedByFirstName(self, pin_fname):
    #     cursor = self.conn.cursor()
    #     query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
    #             "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
    #             "where pin.pin_fname = %s;"
    #     cursor.execute(query, (pin_fname,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # '''Encontrar todas las ordenes de una Persona'''
    #
    # def getOrdersByPersonInNeedByFullName(self, pin_fname, pin_lname):
    #     cursor = self.conn.cursor()
    #     query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
    #             "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
    #             "where pin.pin_fname = %s and pin.pin_lname = %s;"
    #     cursor.execute(query, (pin_fname, pin_lname))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # '''Encontrar todas las ordenes de un suplidor'''
    #
    # def getOrdersBySupplierById(self, s_id):
    #     cursor = self.conn.cursor()
    #     query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
    #             "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
    #             "where supplier.s_id = %s;"
    #     cursor.execute(query, (s_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # '''Encontrar todas las ordenes de un suplidor'''
    #
    # def getOrdersBySuppplierByFirstName(self, s_fname):
    #     cursor = self.conn.cursor()
    #     query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
    #             "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
    #             "where supplier.s_fname = %s;"
    #
    #     cursor.execute(query, (s_fname,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # '''Encontrar todas las ordenes de un suplidor'''
    #
    # def getOrdersBySupplierByFullName(self, s_fname, s_lname):
    #
    #     cursor = self.conn.cursor()
    #     query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
    #             "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier " \
    #             "where supplier.s_fname = %s and supplier.s_lname = %s;"
    #     cursor.execute(query, (s_fname, s_lname))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def checkusername(self, us):
    #     cursor = self.conn.cursor()
    #     query = "select a_password from account where a_username = %s"
    #     cursor.execute(query, (us,))
    #     result = cursor.fetchone()
    #     return result
    #
    # def getUserProfile(self, personid):
    #     cursor = self.conn.cursor()
    #     query = "Select s_fname, s_lname, s_phone, addressline1, city, country, district, zipcode " \
    #             "from account as ac natural inner join supplier as sup natural inner join addresses as ad " \
    #             "where ac.a_id = sup.sa_id " \
    #             "AND sup.saddress_id = ad.address_id " \
    #             "AND sup.s_id = %s;"
    #     cursor.execute(query, (personid,))
    #     result = cursor.fetchone()
    #     return result
    #
    # def getUserKeys(self, username):
    #     cursor = self.conn.cursor()
    #     query = "Select s_id, address_id, a_id, a_username, a_password " \
    #             "from account natural inner join supplier natural inner join addresses " \
    #             "where account.a_id = supplier.sa_id " \
    #             "AND supplier.saddress_id = addresses.address_id " \
    #             "AND account.a_username = %s;"
    #     cursor.execute(query, (username,))
    #     result = cursor.fetchone()
    #     account_type = "supplier"
    #     if result:
    #         result = result + (account_type,)
    #         return result
    #     cursor = self.conn.cursor()
    #     query = "Select pin_id, address_id, a_id, a_username, a_password " \
    #             "from account natural inner join pin natural inner join addresses " \
    #             "where account.a_id = pin.pina_id " \
    #             "AND pin.pinaddress_id = addresses.address_id " \
    #             "AND account.a_username = %s;"
    #     cursor.execute(query, (username,))
    #     result = cursor.fetchone()
    #     account_type = "pin"
    #     if result:
    #         result = result + (account_type,)
    #         return result
    #     cursor = self.conn.cursor()
    #     query = "Select ad_id, address_id, a_id, a_username, a_password " \
    #             "from account natural inner join admins natural inner join addresses " \
    #             "where account.a_id = admins.ada_id " \
    #             "AND admins.adaddress_id = addresses.address_id " \
    #             "AND account.a_username = %s;"
    #     cursor.execute(query, (username,))
    #     result = cursor.fetchone()
    #     account_type = "admin"
    #     result = result + (account_type,)
    #     return result
    #
    # def get_account_id(self, us):
    #     cursor = self.conn.cursor()
    #     query = "select a_id from account where a_username = %s;"
    #     cursor.execute(query, (us,))
    #     result = cursor.fetchone()
    #     return result
    #
    # def get_person_id(self, a_id):
    #     cursor = self.conn.cursor()
    #     query = "select pin_id from pin where pina_id = %s;"
    #     cursor.execute(query, (a_id,))
    #     result = cursor.fetchone()
    #     if not result[0] == None:
    #         return result[0]
    #     query = "select s_id from supplier where sa_id = %s;"
    #     cursor.execute(query, (a_id,))
    #     result = cursor.fetchone()
    #     if not result[0] == None:
    #         return result[0]
    #     query = "select ad_id from admins where ada_id = %s;"
    #     cursor.execute(query, (a_id,))
    #     result = cursor.fetchone()
    #     if not result[0] == None:
    #         return result[0]
    #     return None
    #
    # def create_account(self, us, pw):
    #     cursor = self.conn.cursor()
    #     query = "insert into account(a_username, a_password)values(%s, %s);"
    #     cursor.execute(query, (us, pw,))
    #     self.conn.commit()
    #     query = "select a_id from account where a_username= %s AND a_password= %s;"
    #     cursor.execute(query, (us, pw,))
    #     result = cursor.fetchone()
    #     self.conn.commit()
    #     if not result[0] == None:
    #         return result[0]
    #     return None
    #
    # def insert_product_to_OrderDetails(self, od_qty, od_price, o_id, pin_id, s_id, ba_id, p_id):
    #     cursor = self.conn.cursor()
    #     query = "insert into orderdetails(od_qty, od_pprice, o_id, s_id, ba_id, p_id, pin_id) values (%s, %s, %s, %s, %s, %s, %s) returning od_id;"
    #     cursor.execute(query, (od_qty, od_price, o_id, s_id, ba_id, p_id, pin_id,))
    #     od_id = cursor.fetchone()[0]
    #     self.conn.commit()
    #
    #     return od_id
    #
    # # def create_order(self, cid, date):
    # #     cursor = self.conn.cursor()
    # #     query = "insert into orders(c_id, o_date)values(%s, %s) returning o_id;"
    # #     cursor.execute(query, (cid, date,))
    # #     self.conn.commit()
    # #     result = cursor.fetchone()[0]
    # #     return result
    # '''Return all order info'''
    #
    # def getAllOrders(self):
    #     cursor = self.conn.cursor()
    #     query = "select o_id, od_id, od_qty, od_pprice, s_id, ba_id, p_id, p_name, pin_id, pin_fname, pin_lname, c_id, o_date " \
    #             "from orders natural inner join orderdetails natural inner join product natural inner join pin natural inner join supplier;"
    #
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result