from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.agents.basic_agent import BasicAgent

# 🚀 Initialize FastAPI app
app = FastAPI()

# 🌐 Enable CORS (for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🤖 Initialize AI Agent
agent = BasicAgent()

# 📥 Request schema
class QueryRequest(BaseModel):
    query: str

# 🏠 Health check route
@app.get("/")
def home():
    return {"message": "Logistics AI Agent API is running"}

# 💬 Main AI endpoint
@app.post("/ask")
def ask_agent(request: QueryRequest):
    response = agent.run(request.query)
    return {"response": response}