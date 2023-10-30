# Consigna 3 de Lucas
import datetime
pedidos = open( "pedidos.txt", "w")

with pedidos as archivo:
    while True:
            n_pedidos = input("Ingrese número de pedido (0 termina el programa): ")
            if n_pedidos == str(0):
                print ("Ingreso el número 0, se guardaron los número de pedidos en pedidos.txt")
                print ("Programa terminado.")
                break
            else:
                fecha = datetime.date.today()
                hora = datetime.datetime.now()
                archivo.write(f"Pedido: {n_pedidos} Hora:{hora.strftime('%H:%M')} Fecha:{fecha.strftime('%Y-%m-%d')}\n")
                print("Escribiendo el número: ", n_pedidos)
