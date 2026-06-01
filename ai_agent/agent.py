from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.tools import tool
import requests
import os

load_dotenv()

@tool                       #@tool decorator function ને LangChain Tool બનાવે છે.
def get_weather(city: str): 
    """Return current weather of a city."""
    
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    
    return response.json()['current_condition'][0]["FeelsLikeC"]      #means current_condition na 0 position par feelslike matlab ketla degree che ae tya lakhelu hoi dict ma 

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv('OPENAI_API_KEY')
)

client_with_tools = client.bind_tools([get_weather])          
#હવે LLM ને ખબર પડી:
#મારી પાસે get_weather નામનું tool છે.

response = client_with_tools.invoke(
    "what is the weather in Ahmedabad?"
)

print(response.tool_calls)

if response.tool_calls:               #જો tool call હોય તો અંદર જશે.

    tool_call = response.tool_calls[0]       #First tool call લે છે.
    tool_name = tool_call["name"]               #"get_weather" male 
    tool_arg = tool_call["args"]               # arg ma  "city":"Ahmedabad" male 

    if tool_call["name"] == "get_weather":
        result = get_weather.invoke(tool_arg)
        print(result)

else:
    print(response.content)