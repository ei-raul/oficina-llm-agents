from src.models import llm_gpt, llm_gemini
from src.tools import current_datetime

gpt_with_tools = llm_gpt.bind_tools([current_datetime])
gemini_with_tools = llm_gemini.bind_tools([current_datetime])

print("="*30)
resp_gpt = gpt_with_tools.invoke("Que dia da semana e do mês é hoje?")
print(f">> Resposta GPT:\n{resp_gpt.content}")
print(f">> Ferramentas GPT:\n{resp_gpt.tool_calls}")
print("="*30)

print("="*30)
resp_gemini = gemini_with_tools.invoke("Que dia da semana e do mês é hoje?")
print(f">> Resposta Gemini:\n{resp_gemini.text}")
print(f">> Ferramentas Gemini:\n{resp_gemini.tool_calls}")
print("="*30)
