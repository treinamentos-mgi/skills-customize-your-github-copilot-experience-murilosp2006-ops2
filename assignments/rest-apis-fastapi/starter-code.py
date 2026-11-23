from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = [
    {"name": "Caderno", "price": 12.5},
    {"name": "Caneta", "price": 3.0},
    {"name": "Mochila", "price": 89.9},
]


class Item(BaseModel):
    name: str
    price: float


# Tarefa 1: defina a rota GET / aqui.


# Tarefa 2: defina as rotas GET /items/{item_id} e GET /items aqui.


# Tarefa 3: defina a rota POST /items aqui.
