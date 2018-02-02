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


    # ######################SEARCH BY REQUESTED######################
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


    ###############SEARCH BY AVAILABILITY###########################################################################
    def getRequestBypinId(self, p_id):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join pin where p_id = %s order by r_pname;"
        cursor.execute(query, (p_id,))
        result = cursor.fetchone()
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        cursor = self.conn.cursor()
        query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid


    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from parts where pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid


    def update(self, pid, pname, pcolor, pmaterial, pprice):
        cursor = self.conn.cursor()
        query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        self.conn.commit()
        return pid


    def insert_new_request(self, pin_id, r_pname, r_qty, r_date):
        cursor = self.conn.cursor()
        query = "insert into request(pin_id, r_pname, r_qty, r_date) values (%s, %s, %s, %s) returning r_id;"
        cursor.execute(query, (pin_id, r_pname, r_qty, r_date,))
        request_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_id


    ##### U N U S E D  O R  O B S O L E T E ####

#    def browseResourcesRequested(self):
#        cursor = self.conn.cursor()
#        query = "select * from request natural inner join ain;"
#        cursor.execute(query)
#        result = []
#        for row in cursor:
#            result.append(row)
#        return result