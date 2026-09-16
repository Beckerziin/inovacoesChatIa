# 🤖 Chatbot com Inteligência Artificial

Aplicação web que recebe perguntas do usuário e gera respostas utilizando uma
**API de Inteligência Artificial**. Atividade prática — Centro Universitário FAG.

O usuário digita uma mensagem na interface (React), que é enviada ao backend
(FastAPI). O backend se comunica com a API de IA e retorna a resposta ao usuário.

## 🛠️ Tecnologias

- **Frontend:** React (Vite)
- **Backend:** Python + FastAPI
- **IA:** API de um modelo de IA (compatível com o padrão OpenAI)
- **Comunicação:** API REST utilizando JSON

## 📁 Estrutura

```
ChatIa/
├── backend/          # API em FastAPI
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/         # Aplicação React
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   └── .env.example
└── README.md
```

## 🚀 Como executar

### 1. Backend (FastAPI)

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

pip install -r requirements.txt

# Configure a chave da IA
copy .env.example .env   # Windows  (Linux/Mac: cp .env.example .env)
# edite o arquivo .env e preencha AI_API_KEY

uvicorn main:app --reload
```

O backend ficará disponível em `http://localhost:8000`.

### 2. Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

A aplicação ficará disponível em `http://localhost:5173`.

## ⚙️ Configuração da API de IA

No arquivo `backend/.env` defina:

| Variável      | Descrição                                   | Exemplo                          |
| ------------- | ------------------------------------------- | -------------------------------- |
| `AI_API_KEY`  | Sua chave da API de IA                       | `sk-...`                         |
| `AI_BASE_URL` | URL base do provedor (padrão OpenAI)         | `https://api.openai.com/v1`      |
| `AI_MODEL`    | Modelo utilizado                             | `gpt-4o-mini`                    |

Funciona com qualquer provedor compatível com o padrão OpenAI. Exemplos:

- **OpenAI** — `https://api.openai.com/v1` · modelo `gpt-4o-mini`
- **Groq** (gratuito) — `https://api.groq.com/openai/v1` · modelo `openai/gpt-oss-20b` (veja os modelos disponíveis em `console.groq.com`)
- **OpenRouter** — `https://openrouter.ai/api/v1`

## 📡 Endpoint da API

`POST /api/chat`

```json
// Requisição
{ "message": "Olá, tudo bem?" }

// Resposta
{ "reply": "Olá! Estou bem, e você?" }
```

## ✅ Requisitos atendidos

- [x] Campo para o usuário digitar a mensagem
- [x] Botão para enviar a pergunta
- [x] Integração entre frontend e backend
- [x] Integração do backend com uma API de IA
- [x] Exibição da resposta gerada pela IA
- [x] Interface simples e organizada
