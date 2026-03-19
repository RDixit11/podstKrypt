import socket
import dh

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 1234))

n = dh.get_prime()
while dh.check_prime(n) != True:
    n = dh.get_prime()

n = str(n)

s.send(f"{n}".encode())

y = random.randint(100000, 999999)

s.close()
