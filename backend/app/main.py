from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import upload,qa


app=FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                    )

app.include_router(upload.router,prefix="/upload",tags=["upload"])
app.include_router(qa.router,prefix="/qa",tags=["Q&A"])