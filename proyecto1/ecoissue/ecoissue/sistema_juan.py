import datetime

while True:
    pedido = input("Ingrese el número de pedido: ")

    if pedido == "0":
        break
    else:
        cache = open("pedidos_juan.txt", "a")
        cache.write("Pedido: ")
        cache.write(str(pedido))
        cache.write(" Hora: ")
        cache.write(str(datetime.datetime.now()))
        cache.write("\n")
        cache.close()

        print("Escribiendo el número:", pedido)

print("Cerrando Sistema...")
