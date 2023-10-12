# consigna 1:
# crea un programa que solicite numero de pedido. si este es = 0, fin.
# else, almacenar los numeros de pedido en el archivo pedidos.txt
#


# consigna 2:
# modifique su sistema para que, ademas de escribir en un archivo, ahora imprima
# por pantalla cada número que se ingreso por teclado. y la leyenda:
# Escribiendo el número : xxxx
# adicionalmente el archivo de texto donde se encuentran los números escritos
# debe tener no solo el número, si no que un texto "pedido".
# ej:
# pedido: 1
# pedido: 45
# pedido: 23
# ....
# Ayuda:
# puede utilizar la sintaxis f de strings para incluír el valor de las
# variables dentro del string a imprimir/escribir
# ej:   f"Esto es un string con la variable {variable}"


while True:
    n_pedido = input(str("Ingrese el nº de pedido :"))

    if n_pedido == "0":
        break
    else:
        archivo = open("pedidos.txt", "a")
        archivo.write(str(n_pedido))
        archivo.write("\n")
        archivo.close()
