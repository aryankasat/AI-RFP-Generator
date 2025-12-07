class RFP:

    request_for_proposal = []

    def __init__(self):
        pass

    def add_rfp(self,id,name,content):
        try:
            rfp = {"id":id,"name":name,"content":content,"vendor_data":[]}
            RFP.request_for_proposal.append(rfp)
            return RFP.request_for_proposal
        except Exception as e:
            print ("Error is:",e)
            print ("Error in adding the rfp")

    def modify_rfp(self,id,content):
        pass
    
    def delete_rfp(self,id):
        pass

    
    def retrieve_all_rfp(self):
        try:
            return RFP.request_for_proposal
        except Exception as e:
            print ("Error is:",e)
            print ("Error in retrieving the rfp")

    def display_all_rfp(self):
        try:
            for rfp in RFP.request_for_proposal:
                print (f"Name:{rfp.name} and the content:{rfp.content}")
            return None
        except Exception as e:
            print ("Error is:",e)
            print ("Error in displaying the rfp")