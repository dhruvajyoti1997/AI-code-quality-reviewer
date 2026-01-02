import os
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI

load_dotenv()

def get_llm():
    return OpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
