import socket
import pickle

def get_user_input():
    numbers = input("Enter a set of numbers separated by spaces: ")
    choice = input("Enter your choice (search, sort, split, exit): ")
    return numbers, choice

def main():
    server_ip = "127.0.0.1"
    server_port = 9996

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        numbers, choice = get_user_input()
        data = {'numbers': list(map(int, numbers.split())), 'choice': choice}

        if choice == "exit":
            client_socket.send(pickle.dumps(data))
            break

        if choice in ["search", "sort", "split"]:
            if choice == "search":
                target = int(input("Enter the number to search: "))
                data['target'] = target
            elif choice == "sort":
                ascending = input("Sort in ascending order? (y/n): ").lower() == "y"
                data['ascending'] = ascending

            client_socket.send(pickle.dumps(data))
            server_response = client_socket.recv(1024)
            result = pickle.loads(server_response)

            print("Server response:", result)
        else:
            print("Invalid choice. Please choose from search, sort, split, or exit.")

    client_socket.close()

if __name__ == "__main__":
    main()
