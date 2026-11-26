from src.models import llm_gpt, llm_gemini

print("="*30)
resp_gpt = llm_gpt.invoke([
    ("system", "Você é um professor de computação. Responda em até 2 frases."),
    ("human", "O que é temperatura em um LLM?"),
])
print(f">> Resposta GPT:\n{resp_gpt.content}")
print("="*30)

print("="*30)
resp_gemini = llm_gemini.invoke([
    ("system", "Você é um professor de computação. Responda em até 2 frases."),
    ("human", "O que é temperatura em um LLM?"),
])
print(f">> Resposta Gemini:\n{resp_gemini.text}")
print("="*30)