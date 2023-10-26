import json
with open("/tmp/pedidos.txt") as archivo:
    contenido = archivo.read()
    print(contenido)
    datos = json.loads(contenido)

    for n in datos:
        print(n["numero"])

