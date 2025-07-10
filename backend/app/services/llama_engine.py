import os
from dotenv import load_dotenv

from llama_index.core import (
    VectorStoreIndex,
    Document,
    Settings
)
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding

load_dotenv()

GEMINI_API_KEY=os.getenv("GOOGLE_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Google API key is not found!")

llm = Gemini(api_key=GEMINI_API_KEY, model="models/gemini-2.0-flash")

embed_model=GeminiEmbedding(
    model_name="models/embedding-001",api_key=GEMINI_API_KEY
)

Settings.llm=llm
Settings.embed_model=embed_model

def build_index_from_text(text:str)->VectorStoreIndex:
    doc=Document(text=text)
    index=VectorStoreIndex.from_documents([doc])
    return index

def query_pdf_index(index:VectorStoreIndex,question:str)->str:
    query_engine=index.as_query_engine()
    response=query_engine.query(question)
    return str(response)