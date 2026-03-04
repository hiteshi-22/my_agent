import os
import requests
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

# Load environment variables
load_dotenv()
OMDB_BASE_URL = os.getenv("OMDB_BASE_URL")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

def movie(title: str) -> dict[str, any]:
    """
    This tool fetches the movie information.
    """
    # Build the request URL using env values
    url = f"{OMDB_BASE_URL}?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url) 
    data = response.json()         
    
    print(data)
    return data

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[movie]
)
