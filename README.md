# AI-RFP-Generator

### In order to run application
```bash
pip install -r requirements.txt
```
```bash
uvicorn main:app --reload
```
### Sample queries to run along wit the APIs to which it has to be passed

```bash
/user_query
{
  "id": 1,
  "name" : "Shefali Kasat",
  "user_query" : "I need to procure laptops and monitors for our new office. Budget is $50,000 total. Need delivery within 30 days. We need 20 laptops with 16GB RAM and 15 monitors 27-inch. Payment terms should be net 30, and we need at least 1 year warranty."
}
```
```bash
/get_vendor_list
No payload.
```
```bash
/send_mail
{
"id":1,
"name" : "Aryan Kasat",
"vendor_mail_ids" : ["20uec034@lnmiit.ac.in"]
} 
```
