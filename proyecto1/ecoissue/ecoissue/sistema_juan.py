import datetime

lista = []

while True:
    pedido = {}

    numero = input("Ingrese el número de pedido: ")

    if numero == "0":
        break
    else:
        print("Escribiendo el número:", numero)
        # pedido = {"Numero":numero,"Hora":str(datetime.datetime.now())}
        pedido["Numero"] = numero
        pedido["Hora"] = str(datetime.datetime.now())
        print(pedido)
        lista.append(pedido)

print(lista)
print("Almacenando datos en archivo...")

for item in lista:
    cache = open("pedidos_juan.txt", "a")
    cache.write("Pedido: ")
    cache.write(item.get("Numero"))
    cache.write(" Hora: ")
    cache.write(item.get("Hora"))
    cache.write("\n")
    cache.close()

print("Cerrando Sistema...")
