from enum import Enum


class OrderStatus(Enum):
    RECEBIDO = 'RECEBIDO'
    PENDENTE = 'PENDENTE'
    PROCESSANDO = 'PROCESSANDO'
    CONCLUIDO = 'CONCLUIDO'
    CANCELADO = 'CANCELADO'
