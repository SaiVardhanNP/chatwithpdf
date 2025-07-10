from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from app.services.llama_engine import build_index_from_text, query_pdf_index

router=APIRouter()

class QueryRequest(BaseModel):
    text:str
    question:str
    
class QueryResponse(BaseModel):
    answer:str
    

@router.post("/query",response_model=QueryResponse)
async def query_pdf(request:QueryRequest):
    try:
        index=build_index_from_text(request.text)
        
        answer=query_pdf_index(index,request.question)
        
        return QueryResponse(answer=answer)

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
