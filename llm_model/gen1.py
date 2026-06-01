   # only one question ask then use it .

from openai import OpenAI          #OpenAI models સાથે communicate કરવા માટે.
from dotenv import load_dotenv       #.env file માંથી environment variables load કરવા

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')       #.env file માંથી API key વાંચે છે.OpenAI server સાથે connection બનાવે છે.#ત્યારબાદ requests મોકલી શકાય.
)

response = client.responses.create(            #OpenAI model ને request મોકલે છે.
    model="gpt-3.5-turbo",
    instructions="act as my helpful assistant",
    input= input("enter your question : ")
)

print(response.output_text)

#response bau moto ave atle aene nano karava apde output only text ma lidhu atke answer nano ave .

