import mysql.connector
import logging


class Database:
    def __init__(self, host, user, password, db_name, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.cnx = None
    

    def connect(self):

        if self.cnx != None:
            return
        
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, 
                                host=self.host, port=3306, database=self.db_name, ssl_ca="{ca-cert filename}", 
                                ssl_disabled=False)
        
    def close(self):
        if self.cnx is None:
            return
        
        if not self.cnx.is_connected():
            self.cnx = None
            return
        self.cnx.close()
        self.cnx = None


    def execute(self, sql):
        last_row_id = -1
        try:
            with self.cnx.cursor() as cursor:
                cursor.execute(sql)
            self.cnx.commit()
            last_row_id = cursor.lastrowid
            logging.debug(f"execute last_row_id : {last_row_id}")

        except Exception as e:
            logging.error(e)

        finally:
            return last_row_id
        
    
    def select_one(self, sql):
        result = None
        
        try:
            with self.cnx.cursor(dictionary=True) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        
        except Exception as e:
            logging.error(e)

        finally:
            return result
        

    def select_one(self, sql):
        result = None

        try:
            with self.cnx.cursor(dictionary=True) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()

        except Exception as e:
            logging.error(e)

        finally:
            return result
        

    def select_all(self, sql):
        result = None

        try:
            with self.cnx.cursor(dictionary=True) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()

        except Exception as e:
            logging.error(e)

        finally:
            return result
        
    