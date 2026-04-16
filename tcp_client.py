import socket

def iniciar_cliente():
    # 1. Crear socket y conectar
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 5000))

    # 2. Enviar mensaje
    mensaje = "Hola Servidor, soy el Cliente TCP."
    cliente.send(mensaje.encode('utf-8'))

    # 3. Recibir respuesta
    respuesta = cliente.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {respuesta}")

    # 4. Cerrar
    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()