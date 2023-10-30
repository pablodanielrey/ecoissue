#Consigna 4 de Lucas
# modifique el programa anterior para que en vez de escribir los números
# a un archivo, ahora los vaya guardando en memoria en una variable.
# y cuando el usuario ingrese 0 entonces antes de terminar el programa, 
# escriba todo a un archivo.
# ayuda:
# puede usar un diccionario para almacenar numero y fecha, y una lista para
# almacenar esos diccionarios a medida que se van ingresando.

import datetime
fecha = datetime.date.today()
hora = datetime.datetime.now()
pedidos_final=[]  #Lista

with open( "pedidos.txt", "w") as archivo:
    while True:
            n_pedidos = input("Ingrese número de pedido (0 termina el programa): ")
            ########### Diccionario #########
            pedidos ={
                    "número" : n_pedidos,
                    "fecha" : fecha.strftime('%d-%m-%Y'),
                    "hora" : hora.strftime('%H:%M'),
                }
            ########### Diccionario #########
            if n_pedidos == str(0):
                print ("Ingreso el número 0, se guardaron los número de pedidos en pedidos.txt")                    
                print ("Programa terminado.")
                break
            else:
                pedidos_final.append(pedidos)                                    
                archivo.write(f"Pedido: {n_pedidos} Hora:{hora.strftime('%H:%M')} Fecha:{fecha.strftime('%d-%m-%Y')}\n")
                print("Escribiendo el número: ", n_pedidos)
                print(pedidos)


