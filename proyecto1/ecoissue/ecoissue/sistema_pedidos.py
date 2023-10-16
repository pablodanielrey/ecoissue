
#Archivo Maria Paz.
from datetime import datetime


while True:
    
    n_pedido = input(str("Ingrese el nº de pedido :"))
    fh = datetime.now()
    almacenamiento ={
        'numero' : n_pedido,
        'fecha' : fh
    }
    print("Escribiendo el numero: ", almacenamiento["numero"])

    if almacenamiento["numero"] == "0":

        break
    else:
        archivo = open("/tmp/pedidos.txt", "a")
        archivo.write(str(f"Pedido {almacenamiento['numero']} fecha y hora {almacenamiento['fecha']}"))
        archivo.write("\n")
        archivo.close()