import json

with open("/tmp/pedidos.txt") as archivo:
        
        for linea in archivo.readlines():
            dato = json.loads(linea) 
             
            print("El pedido es: ", dato["numero"])
