# consigna 7:
# debe modificar el programa 1 (que escribe los datos de pedidos)
# para que el archivo almacenado sea un json válido.
# y agregue la siguente informacion a la que ya esta alamacenando
# fecha y hora de la ejecución del programa (cuando se inicia y se comienza a preguntar
# por pedidos)
# debe modificar tambien el programa que muestra los pedidos a partir del archivo
# para adecuarlo al nuevo formato de archivo a leer. y debe imprimir cuando se 
# cargo la información.

import datetime
import json
fecha_time = datetime.datetime.now()
hora_time = datetime.datetime.today()
fecha = fecha_time.strftime("%d,%m,%Y")
hora = hora_time.strftime("%H,%M")
###### Diccionario para cuando se ejecunta el programa ########
info_ejecucion_json = {
    "Fecha de ejecución: " : fecha,
    "Hora de ejecución: " : hora,
    "pedidos_final" : []  #Lista para almacenar los pedidos
}
###### Diccionario para cuando se ejecunta el programa ########

with open( "pedidos.json", "a") as archivo:
    while True:
        try:
            n_pedidos = int(input("Ingrese número de pedido(0 para terminar el programa): "))
            if n_pedidos == 0:
                print ("Ingreso el número 0, se guardaron los número de pedidos en pedidos.json")                    
                print ("Programa terminado.")
                break
        except:
            print("No es un número de pedido válido. Por favor ingrese uno válido.")
        else:
             ####### Diccionario de los pedidos #######
            pedidos = {
            "número: " : n_pedidos,
            "Fecha: " : fecha,
            "Hora: " : hora,
            }
            ####### Diccionario de los pedidos #######
        info_ejecucion_json["pedidos_final"].append(pedidos)
with open ("pedidos.json", "w") as archivo_json:
    json.dump(info_ejecucion_json, archivo_json, indent=4)
    print("Escribiendo los pedidos en el archivo JSON")
    print("Fecha de ejecución: " , info_ejecucion_json["Fecha de ejecución: "])
    print("Hora de ejecución: " , info_ejecucion_json["Hora de ejecución: "],"\n")



with open ("pedidos.json", "r") as archivo_json:
    info_ejecucion_json = json.load (archivo_json)
for pedidos in info_ejecucion_json["pedidos_final"]:
    n_pedidos = pedidos.get("número: ", "Fecha: ")
    print("Número de pedido: ",n_pedidos, "Fecha: ", fecha, "Hora: ", hora)
print("Estos son todos los pedidos guardados")