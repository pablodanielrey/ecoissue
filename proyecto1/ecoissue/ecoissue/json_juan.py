import json

with open("pedidos.json", "r") as archivo:
    listado = json.load(archivo)

    print ("Carga de pedidos \n Inicio: " + listado.get("inicio") +"\n Fin: " + listado.get ("fin") )
    
    for item in listado.get("pedidos"):
        print("Pedido: " + item.get("Numero"))
