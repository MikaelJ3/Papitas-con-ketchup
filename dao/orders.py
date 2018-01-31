from config.dbconfig import pg_config
import psycopg2


class OrdersDao:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def create_new_order(self, c_id, o_date):
        cursor = self.conn.cursor()
        query = "insert into orders(c_id, o_date)values(%s, %s) returning o_id;"
        cursor.execute(query, (c_id, o_date,))
        self.conn.commit()
        result = cursor.fetchone()[0]
        return result