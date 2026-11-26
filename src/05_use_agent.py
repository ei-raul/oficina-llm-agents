from src.agent import build_agent
from src.tools import data_hora_atual

tools = [data_hora_atual]
agent = build_agent(tools)
question = "Que dia da semana e do mês é hoje?"
result = agent.invoke({"messages": [("human", question)]})

for msg in result["messages"]:
    msg.pretty_print()
