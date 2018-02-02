from config.dbconfig import pg_config
import psycopg2


class peopledao:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    '''Return everyone registered as person in need'''

    def getAllPeopleInNeed(self):
        cursor = self.conn.cursor()
        query = "select * from pin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''Return everyone registered as supplier'''

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    '''Return everyone registered as admin'''

    def getAllAdmin(self):
        cursor = self.conn.cursor()
        query = "select * from admin;"
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

    def getPINByFirstName(self, pin_fname):
        cursor = self.conn.cursor()
        query = "Select * " \
                "from pin " \
                "where pin_fname = %s ;"
        cursor.execute(query, (pin_fname,))
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