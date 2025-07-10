from fastapi import APIRouter


router=APIRouter()


@router.get("/")
async def qa():
    return {"msg":"Q&A route is working fine!"}