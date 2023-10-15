import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        user_input = input("Enter a string (or 'Stop' to quit): ")
        client_socket.send(user_input.encode())

        if user_input == "Stop":
            break

        response = client_socket.recv(1024).decode()
        print("Server Response:\n" + response)

    client_socket.close()

if __name__ == "__main__":
    main()
