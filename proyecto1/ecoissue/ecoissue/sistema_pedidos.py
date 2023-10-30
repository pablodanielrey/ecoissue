#Archivo Maria Paz.
from datetime import datetime
import json

lista = []
inicio = datetime.now()#iniciar
print(inicio)
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
        
archivo = open("/tmp/pedidos.json", "w")
for elemento in lista:
    archivo.write(json.dumps(elemento)) #texto = str(f"Pedido {elemento['numero']} fecha y hora {elemento['fecha']}")
    archivo.write("\n")
archivo.close()
fin = datetime.now()
print(fin)
