import socket

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiou"
    s = s.lower()
    count = {vowel: 0 for vowel in vowels}
    for char in s:
        if char in vowels:
            count[char] += 1
    return count

def main():
    server_ip = "127.0.0.1"
    server_port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        while True:
            data = client_socket.recv(1024).decode()
            if data == "Stop":
                break

            is_pal = is_palindrome(data)
            length = len(data)
            vowels_count = count_vowels(data)

            response = f"Is Palindrome: {is_pal}\nString Length: {length}\nVowel Counts: {vowels_count}"
            client_socket.send(response.encode())

        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
