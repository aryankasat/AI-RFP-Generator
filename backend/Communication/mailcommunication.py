from Communication.communication import Communication
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import imaplib
import email
from email.header import decode_header
from Communication.attachments import Attachments
from dotenv import load_dotenv
import mailtrap as mt

class mailCommunication(Communication):

    def __init__(self):
        load_dotenv()
        self.sender_mail_id = os.getenv("MAIL_USERNAME")

    def send_communication(self,receiver_mail_id, mail_content,mail_subject):
        try:
            mail = mt.Mail(
            sender=mt.Address(email=self.sender_mail_id, name="Mailtrap"),
            to=[mt.Address(email=receiver_mail_id)],
            subject=mail_subject,
            text=mail_content,
            category="Testing",
            )

            client = mt.MailtrapClient(token=os.getenv("SMTP_PASSWORD"))
            response = client.send(mail)

            print(response)
        except Exception as e:
            print ("Error:",e)
            print ("Error in sending mails!!")
    
    def decode_str(s):
        try:
            decoded, enc = decode_header(s)[0]
            if isinstance(decoded, bytes):
                decoded = decoded.decode(enc or "utf-8", errors="ignore")
            return decoded
        except Exception as e:
            print ("Error in decoding the header of the mail!")
    

    def receive_communication(self):
        try:
            mail = imaplib.IMAP4_SSL(os.getenv("IMAP_SERVER"))
            mail.login(self.sender_mail_id, self.sender_password)
        except Exception as e:
            print("Error:", e)
            print ("Error in logging into mail id!!!")

        try:
            mail.select("inbox")
            status, messages = mail.search(None, "UNSEEN")
            vendor_email_content = []
            for msg_id in messages[0].split():
                status, msg_data = mail.fetch(msg_id, "(RFC822)")
                raw_email = msg_data[0][1]

                msg = email.message_from_bytes(raw_email)

                subject = mailCommunication.decode_str(msg["Subject"] or "")

                print("\n=== New Email Received ===")
                print("Subject:", subject)
                print("From:", msg.get("From"))
                print("--------------------------")

                email_body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        pdf_content = Attachments(part)

                        if content_type == "text/plain":
                            email_body = part.get_payload(decode=True).decode(errors="ignore")
                        
                else:
                    email_body = msg.get_payload(decode=True).decode(errors="ignore")
                    
                email_content = "Email body:\n" + email_body + "\n" + "PDF content:\n"+ pdf_content
                vendor_email_content.append(email_content)
            mail.close()
            mail.logout()
            
            return vendor_email_content

        except Exception as e:
            print("Error:", e)
            print ("Error in traversing through the mail!!!")