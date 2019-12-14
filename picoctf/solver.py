import socket 

server = '2019shell1.picoctf.com',3161


def receiver(s):
    while True:
        data = s.recv(1024)
        if not data:
            exit(0)
        print data.rstrip()
        for line in data.splitlines():
            yield line.strip()

def send(s, msg):
    print msg.rstrip()
    s.send(msg)

if __name__ == '__main__':
    s = socket.socket()
    s.connect(server)
    for line in receiver(s):
        if line.startswith('
