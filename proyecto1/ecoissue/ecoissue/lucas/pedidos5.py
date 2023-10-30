# consigna 5:
# modifique el programa para que ahora almacene los pedidos dentro del archivo 
# en formato json.
# ayuda:
# https://docs.python.org/3/library/json.html
# tenga en cuenta que los archivos almacenan strings, por lo que
# es necesario convertir los datos que necesite almacenar a string.


import datetime
import json
fecha_time = datetime.datetime.now()
hora_time = datetime.datetime.today()
fecha = fecha_time.strftime("%d,%m,%Y")
hora = hora_time.strftime("%H,%M")
pedidos_final=[]  #Lista

with open( "pedidos.json", "a") as archivo:
    while True:
        n_pedidos = input("Ingrese número de pedido(0 para terminar el programa): ")
        if n_pedidos == str(0):
            print ("Ingreso el número 0, se guardaron los número de pedidos en pedidos.json")                    
            print ("Programa terminado.")
            break
        else:
             ####### Diccionario #######
            pedidos = {
            "número: " : n_pedidos,
            "Fecha: " : fecha,
            "Hora: " : hora,
            }
            ####### Diccionario #######
        pedidos_final.append(pedidos)
with open ("pedidos.json", "w") as archivo_json:
    json.dump(pedidos_final, archivo_json)
    print("Escribiendo los pedidos en el archivo JSON")