from src.agent import build_agent
from src.tools import data_hora_atual, buscar_coordenadas, clima_atual
from src.models import llm_gpt, llm_gemini

tools = [data_hora_atual, buscar_coordenadas, clima_atual]
agent = build_agent(llm=llm_gemini, tools=tools)

while True:
    message = input("🙍Você: ")
    if message.lower() == "sair":
        break
    result = agent.invoke({"messages": [("human", message)]})
    print(f"🤖 Agente: {result["messages"][-1].content}")

    print("\n===================[LOGS]===================\n\n")
    for msg in result["messages"]:
            msg.pretty_print()
    print("\n============================================\n\n")