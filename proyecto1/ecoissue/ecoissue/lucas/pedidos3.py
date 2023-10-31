# Consigna 3 de Lucas
import datetime

with open( "pedidos.txt", "w") as archivo:
    while True:
            try:
                n_pedidos = int(input("Ingrese número de pedido (0 termina el programa): "))
                if n_pedidos == 0:
                    print ("Ingreso el número 0, se guardaron los número de pedidos en pedidos.txt")
                    print ("Programa terminado.")
                    break
            except:
                 print("No es un número de pedido válido. Por favor ingrese uno válido.")
            else:
                fecha = datetime.date.today()
                hora = datetime.datetime.now()
                archivo.write(f"Pedido: {n_pedidos} Hora:{hora.strftime('%H:%M')} Fecha:{fecha.strftime('%Y-%m-%d')}\n")
                print("Escribiendo el número: ", n_pedidos)
