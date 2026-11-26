from agent import agent

question = "Que dia da semana e do mês é hoje?"
result = agent.invoke({"messages": [("human", question)]})

for msg in result["messages"]:
    msg.pretty_print()
