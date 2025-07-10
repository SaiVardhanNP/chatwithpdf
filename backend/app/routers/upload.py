from fastapi import APIRouter,UploadFile, File, HTTPException
from app.services.pdf_processor import extract_text_from_pdf
import fitz


router=APIRouter()


@router.post("/pdf")
async def upload_pdf(file:UploadFile=File(...)):
    if file.content_type!="application/pdf":
        raise HTTPException(status_code=400,detail="Only pdf files are supported")
    try:
        contents=await file.read()
        text=extract_text_from_pdf(contents)
        
        
        return {"filename":file.filename,"text":text[:1000]}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
