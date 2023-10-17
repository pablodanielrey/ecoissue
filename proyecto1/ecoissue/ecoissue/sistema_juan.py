import datetime
import json

lista = []

while True:
    pedido = {}

    numero = input("Ingrese el número de pedido: ")

    if numero == "0":
        break
    else:
        print("Escribiendo el número:", numero)
        # pedido = {"Numero":numero,"Hora":str(datetime.datetime.now())}
        pedido["Numero"] = str(numero)
        pedido["Hora"] = str(datetime.datetime.now())
        print(pedido)
        lista.append(pedido)

print(lista)
print("Almacenando datos en archivo...")

for item in lista:
    with open("pedidos.json", "w") as archivo:
        json.dump(lista, archivo, indent=4)

print("Cerrando Sistema...")
print("<--- Use json_juan.py para acceder al Json creado --->")
