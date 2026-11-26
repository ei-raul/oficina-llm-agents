from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

llm_gpt = ChatGroq(model="openai/gpt-oss-20b", temperature=0.3)
llm_gemini = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.7)
