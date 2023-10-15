
#Archivo Maria Paz.
from datetime import datetime


while True:
    
    n_pedido = input(str("Ingrese el nº de pedido :"))
    fh = datetime.now()
    print("Escribiendo el numero: ", n_pedido)

    if n_pedido == "0":
        break
    else:
        archivo = open("/tmp/pedidos.txt", "a")
        archivo.write(str(f"Pedido {n_pedido} fecha y hora {fh}"))
        archivo.write("\n")
        archivo.close()
