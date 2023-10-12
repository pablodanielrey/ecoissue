
#Archivo Maria Paz.

while True:

    n_pedido = input(str("Ingrese el nº de pedido :"))
    print("Escribiendo el numero: ", n_pedido)

    if n_pedido == "0":
        break
    else:
        archivo = open("/tmp/pedidos.txt", "a")
        archivo.write(str(n_pedido))
        archivo.write("\n")
        archivo.close()
