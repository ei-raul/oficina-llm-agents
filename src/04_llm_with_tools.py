from src.models import llm_gpt, llm_gemini
from src.tools import data_hora_atual

gpt_with_tools = llm_gpt.bind_tools([data_hora_atual])
gemini_with_tools = llm_gemini.bind_tools([data_hora_atual])

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
