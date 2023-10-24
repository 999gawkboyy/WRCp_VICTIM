import socket
import threading

def send(client_socket):
    while 1:
        message = input()
        if message.strip() == 'quit!':
            client_socket.close()
        client_socket.send(message.encode('utf-8'))

def recv(client_socket):
    while 1:
        response = client_socket.recv(1024).decode('utf-8')
        print(f"서버: {response}")

# 클라이언트 소켓 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nickname = input("nickname: ")
server_ip = input("ip: ")  # 서버의 IP 주소
server_port = 12345

client_socket.connect((server_ip, server_port))

send_handler = threading.Thread(target=send, args=(client_socket,))
send_handler.start()
recv_handler = threading.Thread(target=recv, args=(client_socket,))
recv_handler.start()


while 1: pass