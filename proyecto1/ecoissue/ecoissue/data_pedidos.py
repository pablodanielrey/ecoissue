import json

with open("/tmp/pedidos.txt") as archivo:
        linea = archivo.readline()
        
        for dato in linea:
            dato = json.loads(linea) 
             
            print(dato["numero"])

#corregir el for para que itere en cada linea del archivo. de las dos pruebas solo toma el primero o el segundo 
#movi la variable. 