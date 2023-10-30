import json

with open("pedidos.json", "r") as archivo:
    listado = json.load(archivo)

    print ("Carga de pedidos: " + listado.get("inicio"))
    
    for item in listado.get("pedidos"):
        print("Pedido: " + item.get("Numero"))
