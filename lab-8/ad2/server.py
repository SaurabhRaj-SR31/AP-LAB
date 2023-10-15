import socket
import pickle

def search_number(numbers, target):
    return target in numbers

def sort_numbers(numbers, ascending=True):
    return sorted(numbers) if ascending else sorted(numbers, reverse=True)

def split_odd_even(numbers):
    odd_numbers = [n for n in numbers if n % 2 != 0]
    even_numbers = [n for n in numbers if n % 2 == 0]
    return odd_numbers, even_numbers

def main():
    server_ip = "127.0.0.1"
    server_port = 9996

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        while True:
            client_data = client_socket.recv(1024)
            if not client_data:
                break

            data = pickle.loads(client_data)
            numbers = data['numbers']
            choice = data['choice']

            if choice == "search":
                target = data['target']
                result = search_number(numbers, target)
            elif choice == "sort":
                ascending = data['ascending']
                result = sort_numbers(numbers, ascending)
            elif choice == "split":
                odd, even = split_odd_even(numbers)
                result = {"odd": odd, "even": even}
            else:
                result = "Invalid choice"

            response = pickle.dumps(result)
            client_socket.send(response)

        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
