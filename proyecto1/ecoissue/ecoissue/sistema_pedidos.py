# crea un programa que solicite numero de pedido. si este es = 0, fin.
#else, almacenar los numeros de pedido en el archivo pedidos.txt
n_pedido = input("Ingrese el nº de pedido :")

if n_pedido == 0:
    exit()
else:
    n_pedido = open('pedidos.txt' , 'a')
    n_pedido.write(str(n_pedido))
    n_pedido.close()