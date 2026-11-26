from langchain.chat_models import BaseChatModel
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import InMemorySaver # para usar memória
from langchain_core.messages import SystemMessage
from src.models import llm_gpt

# Prompt de sistema (desativado por enquanto). Para usar, descomente e passe
# como `system_prompt` no invoke_llm abaixo.
SYSTEM_PROMPT = """Você é um assistente prestativo que responde sempre em português do Brasil.

Você tem acesso a ferramentas (tools). Use-as da seguinte forma:
- Use `data_hora_atual` sempre que a pergunta depender da data, do dia da semana
  ou da hora atual ou próximas. Nunca adivinhe essas informações.
- Use `buscar_coordenadas` para obter latitude e longitude a partir do nome de
  uma cidade brasileira.
- Use `clima_atual` para obter o clima atual, mas SOMENTE depois de ter a latitude
  e a longitude. Para perguntas sobre o clima de uma cidade, chame primeiro
  `buscar_coordenadas` e depois `clima_atual` com os valores retornados.

Regras:
- Nunca invente valores de argumentos (como coordenadas); obtenha-os pelas tools.
- Só chame uma tool quando ela for realmente necessária para responder.
- Se uma tool retornar erro ou "Cidade não encontrada.", informe o usuário
  em vez de inventar uma resposta.
- Depois de receber os resultados das tools, responda de forma clara e direta,
  citando as unidades (°C, %, mm, km/h).
"""


def build_agent(llm: BaseChatModel = llm_gpt, tools: list = []):
    gpt_with_tools = llm_gpt.bind_tools(tools)

    def invoke_llm(state: MessagesState):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
        # return {"messages": [gpt_with_tools.invoke(state["messages"])]}
        return {"messages": [gpt_with_tools.invoke(messages)]}


    graph = StateGraph(MessagesState)
    graph.add_node("llm", invoke_llm)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "llm")
    graph.add_conditional_edges("llm", tools_condition)
    graph.add_edge("tools", "llm")
    graph.add_edge("llm", END)
    
    return graph.compile()
    # return graph.compile(checkpointer=InMemorySaver())