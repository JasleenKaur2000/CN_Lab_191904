import socket

s=socket.socket()
print('Socket successfully created')
port=56789
s.bind(('',port))
print(f' socket binded to port:{port}')
s.listen(5)
print('Socket is listening')

while True:
    c,address=s.accept()
    print('Got connection from',address)
    message= ('Thank you for connecting')
    c.send(message.encode())
    c.close()