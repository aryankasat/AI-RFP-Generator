from openai import OpenAI
import os
from dotenv import load_dotenv

class LLMCalls:

    def __init__(self,content):
        load_dotenv()
        self.content = content
        self.client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),base_url=os.getenv("BASE_URL"))

    def structure_user_query(self,):
        try:
            response = self.client.responses.create(
                input=f"""Provide a structured representation of the following query such that it can be used for storing and 
                        sending to different vendors in a concise manner. Do not hallucinate as this is extremely critical data.
                        {self.content}
                        """,
                model=os.getenv("MODEL"),
                )
            return response.output_text
        except Exception as e:
            print ("Error :",e)
            print ("The user query could not be structured using LLM!!!")
    
    def structure_vendor_response(self,):
        try:
            response = self.client.responses.create(
                input=f"""Provide a structured representation of the following query such that it can be used for storing 
                        and . Do not hallucinate as this is extremely critical data.
                        {self.content}
                        """,
                model=os.getenv("MODEL"),
                )
            return response.output_text
        except Exception as e:
            print ("Error :",e)
            print ("The vendor query could not be structured using LLM!!!")

    def final_response_generation(self,):
        try:
            response = self.client.responses.create(
                input=f"""Consolidate all the information. Perform accurate reasoning and provide the best vendor among 
                        the given vendors for the given user query.
                        {self.content}
                        """,
                model=os.getenv("MODEL"),
                )
            return response.output_text
        except Exception as e:
            print ("Error :",e)
            print ("The final answer could not be generated using LLM!!!")