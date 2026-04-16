import socket

def iniciar_servidor():
    # 1. Crear socket UDP (SOCK_DGRAM = UDP)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(('localhost', 6000))
    
    print("Servidor UDP listo en el puerto 6000...")

    # 2. Recibir mensaje y dirección del cliente
    datos, direccion = servidor.recvfrom(1024)
    print(f"Mensaje de {direccion}: {datos.decode('utf-8')}")

    # 3. Responder al cliente
    respuesta = "Confirmación UDP enviada."
    servidor.sendto(respuesta.encode('utf-8'), direccion)
    
    servidor.close()

if __name__ == "__main__":
    iniciar_servidor()