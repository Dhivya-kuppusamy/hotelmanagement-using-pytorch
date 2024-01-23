import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    roll_number = input("Enter a roll number: ")
    client_socket.sendto(roll_number.encode(), (HOST, PORT))


