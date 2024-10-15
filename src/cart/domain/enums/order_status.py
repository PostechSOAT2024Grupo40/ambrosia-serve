from enum import Enum


class OrderStatus(Enum):
    RECEBIDO = 3
    PENDENTE = 4
    PROCESSANDO = 1
    CONCLUIDO = 0
    CANCELADO = 5
