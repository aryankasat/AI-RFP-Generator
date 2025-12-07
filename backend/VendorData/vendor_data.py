
class VendorData:

    def __init__(self, request_for_proposal):
        self.request_for_proposal = request_for_proposal

    def insert_vendor_data (self,content,vendor_data):
        try:
            for rfp in self.request_for_proposal:
                if rfp["content"] == content:
                    rfp["vendor_data"].append(vendor_data)
            return self.request_for_proposal
        except Exception as e:
            print ("Error is:",e)
            print ("There is some error in adding vendor data to rfp!!!!")

    def retrieve_vendor_data (self,):
        pass
    
    def display_vendor_data (self,):
        pass

    def delete_vendor_data(self,):
        pass