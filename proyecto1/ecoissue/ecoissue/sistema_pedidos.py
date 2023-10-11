# crea un programa que solicite numero de pedido. si este es = 0, fin.
#else, almacenar los numeros de pedido en el archivo pedidos.txt


while True:
    n_pedido = input("Ingrese el nº de pedido :")
    
    if n_pedido == 0:
        break
else:
    archivo = open('pedidos.txt' , 'a')
    archivo.write(str(n_pedido))   
    archivo.close()
