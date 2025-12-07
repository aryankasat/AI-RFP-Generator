class Vendor:
    
    vendor_list = []

    def __init__(self, ):
        pass

    def add_vendor(self,id,name,mail_ids,content):
        try:
            for mail_id in mail_ids:
                vendor = {"id":id,"name":name, "mail_id":mail_id,"rfp_content":content}
                Vendor.vendor_list.append(vendor)  
            return Vendor.vendor_list
        except Exception as e:
            print ("Error is:",e)
            print ("There is some error in adding vendor data to the list of vendor data!!!!")      

    def remove_vendor(self,id):
        try:
            for vendor in Vendor.vendor_list:
                if vendor.id == id:
                    vendor_to_be_removed = vendor
                    break
            Vendor.vendor_list.remove(vendor_to_be_removed)
            return Vendor.vendor_list
        except Exception as e:
            print ("Error is:",e)
            print ("There is some error in removing vendor data from list!!!!")

    def retrieve_all_vendors(self):
        try:
            return Vendor.vendor_list
        except Exception as e:
            print ("Error is:",e)
            print ("There is some error in retrieving vendor data from list!!!!")
    
    def display_all_vendors(self):
        try:
            for vendor in Vendor.vendor_list:
                print (f"The name of vendor is {vendor.name} and his mail id is {vendor.mail_id}")
        except Exception as e:
            print ("Error is:",e)
            print ("There is some error in displaying vendor data!!!!")
        
