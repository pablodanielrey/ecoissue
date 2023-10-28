import json

with open("/tmp/pedidos.txt") as archivo:
        
        for linea in archivo.readlines():
            dato = json.loads(linea) 
             
            print("El pedido es: ", dato["numero"])

#corregir el for para que itere en cada linea del archivo. de las dos pruebas solo toma el primero o el segundo 
#movi la variable. 