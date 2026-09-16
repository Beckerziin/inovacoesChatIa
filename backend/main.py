"""
Backend do Chatbot com IA - FastAPI

Recebe a mensagem do usuário (frontend), encaminha para uma API de
Inteligência Artificial e devolve a resposta gerada.

A comunicação com a IA usa o SDK da OpenAI, que é compatível com vários
provedores (OpenAI, Groq, OpenRouter, etc.) apenas trocando a base_url.
"""

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

# ---------------------------------------------------------------------------
# Configuração da API de IA (via variáveis de ambiente / arquivo .env)
# ---------------------------------------------------------------------------
AI_API_KEY = os.getenv("AI_API_KEY", "")
AI_BASE_URL = os.getenv("AI_BASE_URL", "https://api.openai.com/v1")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = (
    "Você é um assistente virtual prestativo. "
    "Responda de forma clara, objetiva e em português."
)

app = FastAPI(title="Chatbot IA API", version="1.0.0")

# Libera o acesso do frontend (React) ao backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Modelos de entrada/saída (JSON)
# ---------------------------------------------------------------------------
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


# ---------------------------------------------------------------------------
# Rotas
# ---------------------------------------------------------------------------
@app.get("/")
def health():
    """Verifica se o backend está no ar."""
    return {"status": "ok", "model": AI_MODEL}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """Recebe a mensagem do usuário e retorna a resposta da IA."""
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="A mensagem não pode ser vazia.")

    if not AI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Chave da API de IA não configurada. Defina AI_API_KEY no arquivo .env.",
        )

    client = OpenAI(api_key=AI_API_KEY, base_url=AI_BASE_URL)

    try:
        completion = client.chat.completions.create(
            model=AI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message},
            ],
        )
        reply = completion.choices[0].message.content or ""
    except Exception as exc:  # erro na comunicação com a IA
        raise HTTPException(
            status_code=502,
            detail=f"Erro ao consultar a API de IA: {exc}",
        )

    return ChatResponse(reply=reply.strip())
