import json
with open("/tmp/pedidos.txt") as archivo:
    contenido = archivo.read()
    datos = json.loads(contenido)

    for n in datos:
        print(n["numero"])

