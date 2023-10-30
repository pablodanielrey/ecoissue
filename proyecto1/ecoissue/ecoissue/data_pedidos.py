import json

with open("/tmp/pedidos.json") as archivo:
        
        for linea in archivo.readlines():
            dato = json.loads(linea) 
             
            print("El pedido es: ", dato["numero"])
