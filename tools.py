from datetime import datetime
from langchain.tools import tool

DIAS = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]

@tool
def data_hora_atual() -> str:
    """Retorna o dia da semana, a data e a hora atuais."""
    agora = datetime.now()
    return f"{DIAS[agora.weekday()]}, {agora:%d/%m/%Y %H:%M}"
