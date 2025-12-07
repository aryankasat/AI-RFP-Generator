import mysql.connector
import os 
from dotenv import load_dotenv

class SQLDB:
    
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("SQL_HOST")
        self.user= os.getenv("SQL_USER")
        self.password = os.getenv("SQL_PASSWORD")
        self.database = os.getenv("SQL_DATABASE")
        # self.conn = mysql.connector.connect(
        #         host=self.host,
        #         user=self.user,
        #         password=self.password,
        #         database=self.database
        #     )
        
    def insert_in_sql_db(self,):
        pass

    def retrieve_from_sql_db(self,):
        try:
            # cursor = self.conn.cursor(dictionary=True)
            # query = "SELECT * FROM vendors;"
            # cursor.execute(query)
            # rows = cursor.fetchall() 
            rows = [{"id":0,"name":"Anshul Kasat","mail_id":"anshulkasat25@gmail.com"},{"id":1,"name":"Aryan Kasat","mail_id":"20uec034@lnmiit.ac.in"}]
            return rows
        except Exception as e:
            print ("Error is:",e)
            print ("Error in retrieving the data from the db!!!")

    def delele_from_sql_db(self,id):
        pass

    def modify_from_sql_db(self,id,modified_content):
        pass

        
