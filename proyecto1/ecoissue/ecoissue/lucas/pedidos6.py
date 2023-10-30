# consigna 6:
# cree un nuevo programa para que lea los datos almacenados en consigna 5
# e imprima solo el número de pedido de cada uno de ellos.
# ayuda:
# https://docs.python.org/3/library/json.html
# debe tener ne cuenta que se leen strings de los archivos, por lo que
# hace falta convertirlos a una estructura de datos adecuada para poder
# manipularlos. 

import json

with open( "pedidos.json", "r") as archivo:
    pedidos_final = json.load(archivo)  #carga el archivo json
for pedidos in pedidos_final:
    n_pedidos = pedidos.get("número: ", "Fecha: ")  # asigna una variable y le pide al archivo lo que tiene guardado en "número: "
    print("Número de pedido: ",n_pedidos)
print("Estos son todos los pedidos guardados")