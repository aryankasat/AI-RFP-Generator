from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

class MONGODB:

    def __init__(self,id,name):
        load_dotenv()
        self.password = quote_plus(os.getenv("MONGO_PASSWORD"))
        self.username = os.getenv("MONGO_USERNAME")
        self.address = f"mongodb+srv://{self.username}:{self.password}@rfp-generator.qqjvxgs.mongodb.net/"
        self.client = MongoClient(self.address,tls=True, tlsAllowInvalidCertificates=True)
        self.db_name = self.client[os.getenv("MONGODB_NAME")]
        self.collection = self.db_name[os.getenv("MONOGO_COLLECTION_NAME")]
        self.id = id
        self.name = name

    def insert_in_mongoDB(self,user_query):
        try:
            self.client.admin.command("ping")
            print("MongoDB connection OK")
        except Exception as e:
            print("MongoDB connection failed:", e)
        try:
            query = {"id":self.id,"name":self.name,"user_query":user_query}
            result = self.collection.insert_one(query)
            return result
        except Exception as e:
            print ("Error is:",e)
            print ("Insertion in mongodb was an issue!!!")

    def modify_in_mongodb(self,):
        pass

    def view_in_mongodb(self,):
        pass

    def delele_in_mongodb(self,):
        pass
