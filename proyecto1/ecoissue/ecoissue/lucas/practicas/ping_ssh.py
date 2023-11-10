import paramiko
import getpass
import ping3
import socket


def respond(hostname):
    resp = ping3.ping(hostname)
    return resp

def verifySsh(hostname, username, password, port):
    try:
        ##### Conexión SSH #########
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect ( hostname, port, username, password, timeout=5)
        print("La conexión ssh esta habilitada.")
        # Ejecuta el comando 'hostname' dentro de la sesión SSH
        _, stdout, _ = ssh_client.exec_command('hostname')
        remote_hostname = stdout.read().decode().strip()
        print(f"Nombre del equipo remoto (a través de SSH): {remote_hostname}")
    except paramiko.AuthenticationException:
        print("Error de Autenticación. Verifique las credenciales SSH.")
    except paramiko.SSHException as e:
        print(f"Error de conexión SSH: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")
    finally:
        if ssh_client:
            ssh_client.close()
            

if __name__ == "__main__":
    #####solicita los datos de Conexión SSH #########
    hostname = input("Ingrese la ip del equipo a conectar: ")
    username = str("soporte")
    password = getpass.getpass("Ingrese contraseña de soporte: ")
    port = 22
    
    ####### Realiza el ping #########
    resp = respond(hostname)
    if resp is False:
        print("El equipo no se encuentra encendio. Comuniquese con el usuario.")
    else:
        print("El equipo esta activo. Verificando la conexión por SSH.")
        verifySsh(hostname, username, password, port)