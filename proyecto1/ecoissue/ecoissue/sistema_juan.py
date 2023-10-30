import datetime
import json

lista = []
inicio = str(datetime.datetime.now())

while True:
    pedido = {}

    try:
        numero = int(input("Ingrese el número de pedido: "))
    except:
        print ("Ingrese un número entero, por favor")
        continue

    if numero == 0:
        break
    else:
        print("Escribiendo el número:", numero)
        # pedido = {"Numero":numero,"Hora":str(datetime.datetime.now())}
        pedido["Numero"] = str(numero)
        pedido["Hora"] = str(datetime.datetime.now())
        print(pedido)
        lista.append(pedido)

#print(lista)
listado = {"inicio":inicio, "pedidos":lista}
#print(listado)
print("Almacenando datos en archivo...")

for item in lista:
    with open("pedidos.json", "w") as archivo:
        json.dump(listado, archivo, indent=4)

print("Cerrando Sistema...")
print("<--- Use json_juan.py para acceder al Json creado --->")
