from flask import render_template, request
from application import app
from application.model.dao.pedido_dao import PedidoDAO
from application.model.entity.pedido import Pedido

pedido_dao = PedidoDAO()


@app.route("/pedido")
def pedido():
    return render_template('pedido.html')


@app.route("/pedido", methods=['POST'])
def fazer_pedido():
    valor = request.form['valor']
    quantidade = request.form['quantidade']
    cliente = request.form['cliente']
    pedido = Pedido(cliente,valor,quantidade)
    pedido_dao.pedir(pedido)
    pedido_list = pedido_dao.listar()
    return render_template('pedido.html', pedido_list=pedido_list), 201, {'content-type': "text/html"}
