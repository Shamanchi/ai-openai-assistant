# AI OpenAI Assistant

**AI-ассистент с function calling**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Описание

AI-ассистент на базе OpenAI API с поддержкой:
- Function calling для инструментов
- Настройка модели и температуры
- Асинхронный клиент
- Конфигурация через .env

---

## Быстрый старт
`ash
git clone https://github.com/Shamanchi/ai-openai-assistant
cd ai-openai-assistant
cp .env.example .env
# Добавьте OPENAI_API_KEY
docker-compose up -d
`

### Переменные окружения
| Переменная | Описание |
|------------|----------|
| OPENAI_API_KEY | API ключ OpenAI |
| OPENAI_MODEL | Модель (gpt-4o-mini) |
| OPENAI_TEMPERATURE | Температура |
| MAX_TOKENS | Макс. токенов |
| FUNCTION_CALLING | Включить function calling |

---

## Использование
`python
from app.services.assistant import OpenAIAssistant

assistant = OpenAIAssistant()
response = await assistant.chat('Hello!')
`

---

## Тесты
`ash
pytest -v
`

---

## Docker
`ash
docker build -t ai-openai-assistant .
docker-compose up -d
`

---

## Структура
`
├── app/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── core/logging.py
│   ├── services/assistant.py
│   └── main.py
├── tests/test_api.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
`

---

## CI/CD
GitHub Actions: Ruff, MyPy, Pytest, Docker build

---

## Лицензия
MIT

---

> Источник темы: Каталог портфолио, запись ai-openai-assistant