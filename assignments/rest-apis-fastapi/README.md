# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprender a criar uma API REST com o framework FastAPI em Python, definindo rotas, recebendo parâmetros e validando dados enviados pelo cliente com Pydantic.

## 📝 Tarefas

### 🛠️ Primeira Rota

#### Descrição
Crie uma aplicação FastAPI com uma rota `GET /` que retorna uma mensagem de boas-vindas em JSON. Use o arquivo `starter-code.py` como ponto de partida.

#### Requisitos
O programa concluído deve:

- Criar um objeto `app = FastAPI()`.
- Definir a rota `GET /` retornando `{"message": "Welcome to the API"}`.
- Executar a aplicação com `uvicorn` e acessar a rota pelo navegador ou pelo `/docs`.

### 🛠️ Rotas com Parâmetros

#### Descrição
Crie uma rota que retorne um item da lista `items` pelo seu índice e outra que receba um parâmetro de consulta para filtrar itens.

#### Requisitos
O programa concluído deve:

- Definir `GET /items/{item_id}` retornando o item correspondente.
- Retornar status 404 quando o `item_id` não existir na lista.
- Definir `GET /items` com o parâmetro de consulta opcional `limit` (inteiro) que limita a quantidade de itens retornados.
- Exemplo de uso: `GET /items?limit=2`

### 🛠️ Criar Itens com Pydantic

#### Descrição
Crie uma rota `POST /items` que recebe um item em JSON, valida os dados com um modelo Pydantic e o adiciona à lista.

#### Requisitos
O programa concluído deve:

- Definir uma classe `Item` herdando de `BaseModel`, com os campos `name` (texto) e `price` (número).
- Receber o corpo da requisição como `Item` e adicioná-lo à lista `items`.
- Retornar o item criado com status 201.
- Rejeitar automaticamente, com erro 422, requisições em que `price` não seja um número.
