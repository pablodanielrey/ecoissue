
#Archivo Maria Paz.
from datetime import datetime
fh = datetime.now()

while True:

    n_pedido = input(str("Ingrese el nº de pedido :"))
    print("Escribiendo el numero: ", n_pedido)

    if n_pedido == "0":
        break
    else:
        archivo = open("/tmp/pedidos.txt", "a")
        archivo.write(str(f"Pedido {n_pedido} fecha y hora {fh}"))
        archivo.write("\n")
        archivo.close()
