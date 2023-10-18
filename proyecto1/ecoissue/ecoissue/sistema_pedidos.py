#Archivo Maria Paz.
from datetime import datetime
import json

lista = []
while True:
    n_pedido = input(str("Ingrese el nº de pedido :"))
    fh = str(datetime.now())
    almacenamiento ={
        'numero' : n_pedido,
        'fecha' : fh
    }
    
    print("Escribiendo el numero: ", almacenamiento["numero"])
  
    if almacenamiento["numero"] == "0":
        break
    else:
       
        lista.append(almacenamiento)
        
archivo = open("/tmp/pedidos.txt", "w")
for elemento in lista:
    texto = str(f"Pedido {elemento['numero']} fecha y hora {elemento['fecha']}")

    archivo.write(json.dumps(texto))
    archivo.write("\n")
archivo.close()
