# Consigna 2 de Lucas

pedidos = open( "pedidos.txt", "w")

with pedidos as archivo:
    while True:
            n_pedidos = int(input("Ingrese número de pedido (0 termina el programa): "))
            if n_pedidos == 0:
                print ("Ingreso el número 0, se guardaron los número de pedidos en pedidos.txt")
                print ("Programa terminado.")
                break
            else:
                archivo.write(f"Pedido: {n_pedidos}\n")
                print("Escribiendo el número: ", n_pedidos)
