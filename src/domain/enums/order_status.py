from enum import Enum


class OrderStatus(Enum):
    PENDENTE = "Pendente"
    PROCESSANDO = "Processando"
    CONCLUIDO = "Concluído"
    CANCELADO = "Cancelado"
