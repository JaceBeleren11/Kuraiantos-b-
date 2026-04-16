import socket

def iniciar_servidor():
    # 1. Crear socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Enlazar y escuchar
    servidor.bind(('localhost', 5000))
    servidor.listen(1)
    print("Servidor TCP esperando conexiones en el puerto 5000...")

    # 3. Aceptar conexión
    conexion, direccion = servidor.accept()
    print(f"Conectado con: {direccion}")

    try:
        # 4. Recibir mensaje (hasta 1024 bytes)
        mensaje = conexion.recv(1024).decode('utf-8')
        print(f"Cliente dice: {mensaje}")

        # 5. Enviar respuesta
        respuesta = "Mensaje TCP recibido correctamente."
        conexion.send(respuesta.encode('utf-8'))
    finally:
        # 6. Cerrar conexión
        conexion.close()
        servidor.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    iniciar_servidor()