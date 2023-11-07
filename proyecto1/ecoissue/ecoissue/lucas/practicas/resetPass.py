####### Funciona para WINDOWS, faltaria ponerlo mas identado y hacer que el cambio lo escriba en un txt #######

import paramiko
import getpass


####solicita los datos de Conexión SSH #########
hostname = input("Ingrese la ip del equipo: ")
username = str("soporte")
password = getpass.getpass("Ingrese contraseña de soporte: ")
port = 22

####solicita los datos para resetear la contraseña #########
user = input("Ingrese el usuario al que le quiere cambiar la contraseña: ")
passNew = getpass.getpass("Ingrerse la contraseña Nueva: ")

# Configuración de algoritmos deshabilitados
disabled_algorithms = {'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']}

##### Conexión por SSH #####
try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect ( hostname, port, username, password, disabled_algorithms=disabled_algorithms )
    print(" Conexión establecidad")
except:
    print(" No se Pudo conectar")

# Cambia la contraseña del usuario
command = f'net user {user} {passNew}'
stdin, stdout, stderr = ssh_client.exec_command(command)

# Verifica si la operación fue exitosa
if not stderr.read():
    print(f"La contraseña de {user} se ha cambiado correctamente.")
else:
    print(f"No se pudo cambiar la contraseña de {user}.")

# Cierra la conexión SSH
ssh_client.close()