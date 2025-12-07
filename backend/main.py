from fastapi import FastAPI
import fastapi
import json
from fastapi.responses import JSONResponse,FileResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
from LLMCalls.llmcalls import LLMCalls
from RFP.rfp import RFP
from Storage.rfp_data_mongo import MONGODB
from Storage.vendor_data_sql import SQLDB
from Communication.mailcommunication import mailCommunication
from VendorData.vendor_data import VendorData
from Vendor.vendor import Vendor
from Storage.vendor_data_sql import SQLDB
from dotenv import load_dotenv


load_dotenv()

app=FastAPI()
origins_str = os.environ.get("ALLOWED_ORIGINS","*")
origins = origins_str.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods = ["*"], #allows all http methods
    allow_headers = ["*"] #allows all headers
)

rfp = RFP()
vendor = Vendor()

@app.get("/check_mail")
def check_mail(data:dict):
    id = data["id"]
    name = data["name"]
    mailcommunication = mailCommunication()
    vendor_content = mailcommunication.receive_communication()
    # rfp = RFP(id,name)
    last_user_query = (rfp.retrieve_all_rfp())[-1]
    request_for_proposal = rfp.retrieve_all_rfp()
    vendor_data = VendorData(request_for_proposal)
    
    for content in vendor_content:
        llmcall_for_structuring_vendor_data = LLMCalls(content)
        structured_vendor_data = llmcall_for_structuring_vendor_data.structure_vendor_response()
        request_for_proposal = vendor_data.insert_vendor_data(structured_vendor_data,last_user_query)

    #final comparsion answer
    for rfp in request_for_proposal:
        user_query = rfp["content"]
        vendor_data = rfp["vendor_data"]
        final_llm_query = f"""User asked requirement : {user_query} and Vendor given info : {vendor_data}"""
        llm_call = LLMCalls(final_llm_query)
        final_comparison_output = llm_call.final_response_generation()
        return final_comparison_output

@app.post("/send_mail")
def send_mail(data:dict):
    id = data["id"]
    name = data["name"]
    vendor_mail_ids = data["vendor_mail_ids"]
    print(len(rfp.retrieve_all_rfp()))
    last_user_query = (rfp.retrieve_all_rfp())[-1]
    vendor_list = vendor.add_vendor(id,name,vendor_mail_ids,last_user_query['content'])
        
    for vendor_content in vendor_list:
        mailcommunication = mailCommunication()
        mailcommunication.send_communication(vendor_content["mail_id"],last_user_query['content'],"Request for proposal from ABC Pvt Ltd.")

    return "Communication sent!!!!!"
    
@app.get("/get_vendor_list")
def get_vendor_list():
    sql_connection = SQLDB()
    vendor_data = sql_connection.retrieve_from_sql_db()
    return vendor_data

@app.post("/user_query")
def get_user_query(data:dict):
    id = data["id"]
    name = data["name"]
    user_query = data["user_query"]
    llmcall_for_structuring_user_query = LLMCalls(user_query)
    structured_user_query = llmcall_for_structuring_user_query.structure_user_query()
    print(structured_user_query)
    request_to_proposal = rfp.add_rfp(id,name,structured_user_query)
    #Storage in mongoDB
    mongodb_connection = MONGODB(id,name)
    result = mongodb_connection.insert_in_mongoDB(request_to_proposal[-1])
    print ("Inserted the query - ", result.inserted_id)
    return structured_user_query + "\n" + f"Inserted the query - {result.inserted_id}"

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level='info'
    )