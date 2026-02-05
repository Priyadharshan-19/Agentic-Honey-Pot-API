import os
import json
from google import genai
from google.genai import types
from tenacity import retry, wait_random_exponential, stop_after_attempt, retry_if_exception_type
from dotenv import load_dotenv

load_dotenv()

# Initialize the 2026 unified client
# The SDK automatically uses GEMINI_API_KEY from your environment
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class QuotaExceededError(Exception):
    pass

@retry(
    wait=wait_random_exponential(multiplier=1, max=60),
    stop=stop_after_attempt(3), # Retries 3 times if rate limited
    retry=retry_if_exception_type(QuotaExceededError)
)
def extract_scam_intelligence(message: str):
    """
    Extracts scam intelligence from raw text.
    Addresses the 'Intelligent Logic' criteria with structured output fallback.
    """
    try:
        # Using the stable 2.5 Flash model verified by your script
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a Fraud Analyst. Analyze the message and extract: "
                    "1. category (Phishing, UPI Scam, Job Scam, etc.) "
                    "2. urgency_level (1-10) "
                    "3. tactic (FOMO, Authority, Threat, etc.) "
                    "4. entities (list of links, UPI IDs, or phone numbers)."
                    "Return ONLY a valid JSON object."
                ),
                response_mime_type="application/json", # Ensures strict JSON
                max_output_tokens=2048 # Increased to prevent 'None' response errors
            )
        )
        
        # PRIMARY: Attempt to return the auto-parsed dictionary
        if response.parsed:
            return response.parsed
        
        # FALLBACK: If .parsed is None, manually parse the text content
        if response.text:
            return json.loads(response.text)
            
        return {"error": "Empty AI response", "details": "The model returned no content."}
        
    except Exception as e:
        # Handle 429 Rate Limit errors specifically for the tenacity retry
        if "429" in str(e):
            raise QuotaExceededError("Rate limit hit")
        return {"error": "Extraction failed", "details": str(e)}