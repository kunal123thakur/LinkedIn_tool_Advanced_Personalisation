from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

GROQ_API_KEY = os.getenv("GROK_API_KEY")

load_dotenv()
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)
