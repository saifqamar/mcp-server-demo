from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

apikey = os.getenv("CURRENT_NEWS_API")

# Create an MCP server
mcp = FastMCP("Latest news server")



@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m**2)

@mcp.tool()
def get_user_weight() -> str:
    return "60kg"

@mcp.tool()
async def latest_news() -> str:
    """Fetch latest news"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.currentsapi.services/v1/latest-news", params={'apiKey':apikey, 'language':'en'})
        return response.text

@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello from mcp server, {name}!"

