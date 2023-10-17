import json

with open("pedidos.json", "r") as archivo:
    lista = json.load(archivo)

for item in lista:
    print("Pedido: " + item.get("Numero"))
