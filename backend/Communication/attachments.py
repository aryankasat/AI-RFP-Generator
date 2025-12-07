import os
from email.header import decode_header
from Communication.parsing import Parsing

class Attachments:

    def __init__(self,part):
        self.part = part

    def decode_str(self,s):
        try:
            decoded, enc = decode_header(s)[0]
            if isinstance(decoded, bytes):
                decoded = decoded.decode(enc or "utf-8", errors="ignore")
            return decoded
        except Exception as e:
            print ("Error in decoding the header of the mail!")
    
    def pdf_attachments (self,):
        try:
            filename = self.part.get_filename()
            if filename:
                filename = Attachments.decode_str(filename)

                if filename.lower().endswith(".pdf"):
                    file_path = os.path.join("/Users/aryankasat/Documents/Aryan/Codes/AI based RFP Generator", filename)

                    with open(file_path, "wb") as f:
                        f.write(self.part.get_payload(decode=True))

                    print(f"PDF saved: {file_path}")
                    parser = Parsing(file_path)
                    pdf_content = parser.pdf_parsing()
                    return pdf_content
        except Exception as e:
            print ("No PDF attachment found!!!")

    def word_parsing(self,):
        pass
