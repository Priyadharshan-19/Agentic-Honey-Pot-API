import os
from fastapi import FastAPI, HTTPException, Header, Depends, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from engine import extract_scam_intelligence

load_dotenv()

app = FastAPI(title="Agentic Honey-Pot API")

# Your chosen secret key for the buildathon submission
SUBMISSION_API_KEY = os.getenv("SUBMISSION_API_KEY")

class ScamRequest(BaseModel):
    message: str

def verify_api_key(x_api_key: str = Header(None)):
    """
    Mandatory authentication dependency for the hackathon.
    """
    if not x_api_key or x_api_key != SUBMISSION_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return x_api_key

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Prevents 500 errors by returning structured JSON"""
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal Server Error", "details": str(exc)}
    )

@app.get("/")
def health():
    return {"status": "online", "developer": "Priyadharshan M"}

@app.post("/analyze")
async def analyze(request: ScamRequest, api_key: str = Depends(verify_api_key)):
    """
    Primary endpoint for the automated evaluation system.
    """
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Empty message")
        
    intelligence = extract_scam_intelligence(request.message)
    
    return {
        "success": True,
        "intelligence": intelligence
    }

if __name__ == "__main__":
    import uvicorn
    # Use 0.0.0.0 so the API is accessible on public cloud URLs
    uvicorn.run(app, host="0.0.0.0", port=8000)