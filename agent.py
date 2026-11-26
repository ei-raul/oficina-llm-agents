from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from models import llm_gpt
from tools import data_hora_atual

tools = [data_hora_atual]
gpt_with_tools = llm_gpt.bind_tools(tools)

def invoke_llm(state: MessagesState):
    return {"messages": [gpt_with_tools.invoke(state["messages"])]}

graph = StateGraph(MessagesState)
graph.add_node("llm", invoke_llm)
graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "llm")
graph.add_conditional_edges("llm", tools_condition)
graph.add_edge("tools", "llm")
graph.add_edge("llm", END)

agent = graph.compile()