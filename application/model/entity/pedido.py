class Pedido():
    def __init__(self,cliente,valor,quantidade):
        self._cliente = cliente
        self._valor = valor 
        self._quantidade = quantidade
        self._valor_total = 0
    

    def get_valor(self):
        return self._valor 

    def get_quantidade(self):
        return self._quantidade

    def get_valor_total(self):
        return self._valor_total

    def get_cliente(self):
        return self._cliente

    def set_valor_total(self,valor):
        self._valor_total = valor
        