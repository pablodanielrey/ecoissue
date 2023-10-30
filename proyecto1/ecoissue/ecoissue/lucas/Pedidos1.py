# Consigna 1 de Lucas

with open( "pedidos.txt", "w") as archivo:
    while True:
            n_pedidos = input("Ingrese número de pedido (0 termina el programa): ")
            if n_pedidos == str(0):
                print ("Ingreso el número 0, se guardaron los número de pedidos en pedidos.txt")
                print ("Programa terminado.")
                break
            else:
                archivo.write(f"{n_pedidos}\n")