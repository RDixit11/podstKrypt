import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 1234))
s.listen(1)

conn, addr = s.accept()

data = conn.recv(1024)

print(data.decode())

x = random.randint(100000, 999999) # private key

conn.close()
