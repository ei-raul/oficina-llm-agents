from src.models import llm_gpt, llm_gemini

print("="*30)
resp_gpt = llm_gpt.invoke("Que dia da semana e do mês é hoje?")
print(f">> Resposta GPT:\n{resp_gpt.content}")
print("="*30)

print("="*30)
resp_gemini = llm_gemini.invoke("Que dia da semana e do mês é hoje?")
print(f">> Resposta Gemini:\n{resp_gemini.text}")
print("="*30)