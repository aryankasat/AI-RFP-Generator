from pypdf import PdfReader
class Parsing:

    def __init__(self,file_path):
        self.fil_path = file_path
        
    def pdf_parsing(self,):
        try:

            text_output = []
            reader = PdfReader(self.file_path)

            for page in reader.pages:
                text_output.append(page.extract_text() or "")

            return "\n".join(text_output)
        except Exception as e:
            print ("Error in parsing the PDF")

    def word_parsing (self,):
        pass