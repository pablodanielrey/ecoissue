import json

with open( "pedidos.json", "r") as archivo:
    info_ejecucion_json = json.load (archivo)  #carga el archivo json
for pedidos in info_ejecucion_json:
    info_fecha_json = info_ejecucion_json.get("Fecha de ejecución: ")  # asigna una variable y le pide al archivo lo que tiene guardado
    info_hora_json = info_ejecucion_json.get("Hora de ejecución: ")  # asigna una variable y le pide al archivo lo que tiene guardado
print("Fecha de Ejecución del Programa: ",info_fecha_json)
print("Hora de Ejecución del Programa: ",info_hora_json)