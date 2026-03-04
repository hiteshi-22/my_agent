# LLM Agents Project 
This repository contains AI agents built with Google's Generative AI and Tavily search. The agents can answer user queries by combining LLM capabilities with external tools.

## Agents Covered in this project
1. Basic Agent (`my_agent`):  Agent with 2 made-up tools: Compute the Einstein and Hiteshi representation of an integer. This was to force the LLM to rely on tool calls to answer user's query.
2. Smart Agent (`smart_agent`): Agent that connects to the Tavily API to search across the internet to answer user's query.
3. Calculator Agent (`calc_agent`): Agent with 3 tools: square of a number, compute factorial and cube of a number.
4. Movie Agent (`movie_agent`): Agent that can fetch details of a movie using the OMDB API.

## Environment Variables
The environment variables placeholders are mentioned in the .env.example. You can create your own env file (from .env.example) by providing the API keys. API key can be created by following the below steps:

### Google API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/api-keys) or your Google Cloud Console.
2. Create a new API key.
3. Copy the key and keep it safe.
4. Set the key for the environment variable `GOOGLE_API_KEY` for the agent you are looking to run.

### Tavily API Key
1. Sign up at [tavily.com](https://www.tavily.com/).
2. Generate a developer API key from your account dashboard.
3. Copy the API key to the `.env` file created in `smart_agent`.

### OMDB API Key
1. Sign up at the [Open-Movie-Database](https://www.omdbapi.com/).
2. Create an API key.
3. Copy the API key to the `.env` file created in `movie_agent`.

