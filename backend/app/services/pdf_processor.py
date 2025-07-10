import fitz

def extract_text_from_pdf(file_bytes:bytes)->str:
    try:
        doc=fitz.open(stream=file_bytes,filetype="pdf")
        text=""
        for page in doc:
            text+=page.get_text()
        doc.close()
        
        return text
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from pdf file : {str(e)}")
    