from config.dbconfig import pg_config
import psycopg2


class RequestDAO:
    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['host'],
                                                                    pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin ;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetRequestsByID(self, r_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin " \
                "where r_id = %s order by r_pname;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetRequestsByPNAME(self, r_pname):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin " \
                "where r_pname = %s order by r_pname;"
        cursor.execute(query, (r_pname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetRequestsByDATE(self, r_date):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin " \
                "where r_date = %s order by r_pname;"
        cursor.execute(query, (r_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetRequestsByQTY(self, r_qty):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin " \
                "where r_qty = %s order by r_pname;"
        cursor.execute(query, (r_qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetRequestsByPINID(self, pin_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin " \
                "where pin_id = %s order by r_pname;"
        cursor.execute(query, (pin_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetRequestsByPINFNAME(self, pin_fname):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin " \
                "where pin_fname = %s order by r_pname;"
        cursor.execute(query, (pin_fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def GetRequestsByPINFULLNAME(self, pin_fname, pin_lname):
        cursor = self.conn.cursor()
        query = "select r_id, r_pname, r_qty, r_date, pin_id, pin_fname, pin_lname " \
                "from request natural inner join pin " \
                "where pin_fname = %s and pin_lname = %s order by r_pname;"
        cursor.execute(query, (pin_fname, pin_lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert_new_request(self, pin_id, r_pname, r_qty, r_date):
        cursor = self.conn.cursor()
        query = "insert into request(pin_id, r_pname, r_qty, r_date) values (%s, %s, %s, %s) returning r_id;"
        cursor.execute(query, (pin_id, r_pname, r_qty, r_date,))
        request_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_id

    def update_request(self, r_id, pin_id, r_pname, r_date, r_qty):
        cursor = self.conn.cursor()
        query = "update request set pin_id = %s, r_pname = %s, r_date = %s, r_qty = %s where r_id = %s;"
        cursor.execute(query, (pin_id, r_pname, r_date, r_qty, r_id,))
        self.conn.commit()
        return r_id