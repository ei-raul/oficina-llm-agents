# Oficina LLM Agents

Estudo progressivo: de uma chamada simples a LLM até um agente com LangGraph.

## Pré-requisitos

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- Chave da [Groq](https://console.groq.com/keys) e do [Google AI Studio (Gemini)](https://aistudio.google.com/apikey)

## Configuração

```bash
uv sync
```

Crie um arquivo `.env` na raiz:

```env
GROQ_API_KEY=sua_chave
GEMINI_API_KEY=sua_chave
```

## Execução

Rode sempre **da raiz do projeto**, como módulo:

```bash
uv run python -m src.01_llm
```

## Etapas

| # | Comando | O que mostra |
|---|---------|--------------|
| 1 | `uv run python -m src.01_llm` | Chamada simples a um LLM (Groq/GPT-OSS e Gemini) |
| 2 | `uv run python -m src.02_roles` | Papéis das mensagens: `system` e `human` |
| 3 | `uv run python -m src.03_llm_limit` | Limitação: o LLM não sabe a data atual |
| 4 | `uv run python -m src.04_llm_with_tools` | `bind_tools`: o LLM decide chamar uma ferramenta (`tool_calls`), mas não a executa |
| 5 | `uv run python -m src.05_use_agent` | Agente LangGraph: o loop LLM → ferramenta → LLM gera a resposta final |

## Arquivos de apoio

- [src/models.py](src/models.py): define os LLMs (`llm_gpt`, `llm_gemini`) e carrega o `.env`.
- [src/tools.py](src/tools.py): ferramenta `data_hora_atual`.
- [src/agent.py](src/agent.py): grafo do agente (nós `llm` e `tools`, com roteamento condicional).

## Sugestão de estudo

1. Rode as etapas em ordem e compare as respostas dos dois modelos.
2. Na etapa 4, observe que `tool_calls` vem preenchido, mas a resposta não usa o resultado.
3. Na etapa 5, leia as mensagens impressas (human → AI com tool call → tool → AI final) e relacione com o grafo em `agent.py`.
4. Experimente: criar uma nova ferramenta em `tools.py` e adicioná-la à lista `tools` do agente.
