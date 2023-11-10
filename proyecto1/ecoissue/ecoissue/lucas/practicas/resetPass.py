####### Funciona para WINDOWS #######

import paramiko
import getpass
import datetime


##### Variables para escribir la fecha y la hora de cuando se cambio la clave ########
fecha_time = datetime.datetime.now()
hora_time = datetime.datetime.today()
fecha = fecha_time.strftime("%d,%m,%Y")
hora = hora_time.strftime("%H,%M")

# Configuración de algoritmos deshabilitados
# disabled_algorithms = {'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']}

######### Función para conectar por ssh ############
def verifySsh(hostname, username, password, port):
    try:
        ##### Conexión SSH #########
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect ( hostname, port, username, password, timeout=5)
        print("La conexión ssh esta habilitada.")
        return True
    except paramiko.AuthenticationException:
        print("Error de Autenticación. Verifique las credenciales SSH.")
    except paramiko.SSHException as e:
        print(f"Error de conexión SSH: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")
        return False
  

    ####solicita los datos de Conexión SSH #########
hostname = input("Ingrese la ip o host del equipo a conectar por ssh: ")
username = str("soporte")
password = getpass.getpass("Ingrese contraseña de soporte: ")
port = 22


if verifySsh is True:
    with paramiko.SSHClient() as ssh_client:
        ####solicita los datos para resetear la contraseña #########
        user = input("Ingrese el usuario al que le quiere cambiar la contraseña: ")
        passNew = getpass.getpass("Ingrese la nueva contraseña: ")
            
        # Cambia la contraseña del usuario
        command = f'net user {user} {passNew}'
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Verifica si la operación fue exitosa
        if not stderr.read():
            print(f"La contraseña de {user} se ha cambiado correctamente.")
            ####### Escribe la nueva clave en un archivo txt #######
            with open( "contraseñas.txt", "a") as archivo:
                archivo.write(f"{user}\n Nueva contraseña: {passNew}\n Hora:{hora}\n Fecha:{fecha}\n   -------------\n")
                archivo.close()
        else:
            print(f"No se pudo cambiar la contraseña de {user}.")
                  
# Cierra la conexión SSH
ssh_client.close()


