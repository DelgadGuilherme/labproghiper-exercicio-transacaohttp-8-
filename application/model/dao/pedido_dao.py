class PedidoDAO():
    def __init__(self):
        self._pedido_list = []

    def pedir(self,pedido):
        valor1 = pedido.get_valor()
        valor2 = pedido.get_quantidade()
        pedido.set_valor_total(int(valor1) * int(valor2))
        self._pedido_list.append(pedido)

    def listar(self):
        return self._pedido_list

