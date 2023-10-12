pedido = input("Ingrese el número de pedido: ")

cache = open("pedidos_juan.txt", "a")
cache.write(str(pedido))
cache.write("\n")
cache.close()
