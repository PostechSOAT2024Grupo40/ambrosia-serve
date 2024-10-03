from enum import Enum


class PaymentConditions(Enum):
    CARTAO_CREDITO = "Cartão de Crédito"
    CARTAO_DEBITO = "Cartão de Díbito"
    DINHEIRO = "Dinheiro"
    PIX = "Pix"
