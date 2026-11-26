from datetime import datetime
import httpx
from langchain.tools import tool

DIAS = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]

# Pra usar no passo 04
@tool
def data_hora_atual() -> str:
    """Retorna o dia da semana, a data e a hora atuais."""
    agora = datetime.now()
    return f"{DIAS[agora.weekday()]}, {agora:%d/%m/%Y %H:%M}"

# Pra usar no passo 06
@tool
def buscar_coordenadas(city: str) -> str:
    """Retorna a latitude e a longitude de uma cidade brasileira."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "countryCode": "BR"}
    data = httpx.get(url, params=params, timeout=10).json()
    if "results" not in data:
        return "Cidade não encontrada."
    local = data["results"][0]
    return f"{local['name']}: lat {local['latitude']}, lon {local['longitude']}"

@tool
def clima_atual(latitude: float, longitude: float) -> str:
    """Retorna temperatura (°C), umidade (%), chuva (mm) e vento (km/h) atuais."""
    url = "https://api.open-meteo.com/v1/forecast"
    variaveis = "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
    params = {"latitude": latitude, "longitude": longitude, "current": variaveis}
    dados = httpx.get(url, params=params, timeout=10).json()
    return str(dados["current"])
