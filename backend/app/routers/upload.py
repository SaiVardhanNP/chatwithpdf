from fastapi import APIRouter


router=APIRouter()


@router.get("/")
async def test_upload():
    return {"msg":"Upload route is working fine!"}