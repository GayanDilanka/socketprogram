
import socket
import docker 


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    print(host)
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    print("hello Hi")
    
    client=docker.from_env()
    for image in client.images.list():
        print (image.id)
        break
    
      client=docker.from_env()
    for image in client.images.list():
        print (image.id)
        break
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client
        print("hello Hi")
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
