import socket

HOST = '127.0.0.1'
PORT = 12345

student_details = {
    '21CSR039': 'Dharshini.K,228,kaveri ',
    '21CSR041': 'dhivya, 106, bhavani',
    '21CSR031': 'dhanusika,189, amaravathi',
    '21CSR064': 'harsha, 186, kaveri',
}

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print("Server listening on", HOST, "port", PORT)

    while True:
        data, addr = server_socket.recvfrom(1024)
        roll_number = data.decode('utf-8')

        if roll_number in student_details:
            print(student_details[roll_number])
        else:
            print("Student not found.")

