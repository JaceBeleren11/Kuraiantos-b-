import socket

def iniciar_cliente():
    # 1. Crear socket
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor_dir = ('localhost', 6000)

    # 2. Enviar mensaje sin conexión previa
    mensaje = "Hola, esto es un datagrama UDP."
    cliente.sendto(mensaje.encode('utf-8'), servidor_dir)

    # 3. Recibir respuesta
    datos, direccion = cliente.recvfrom(1024)
    print(f"Respuesta del servidor: {datos.decode('utf-8')}")

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()