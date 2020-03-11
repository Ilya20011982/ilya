from datetime import datetime
import socket

headers = '''HTTP/1.1 {} {}
Date: Fri, 06 Mar 2020 {:02}:{:02}:{:02} GMT
Content-Type: text/html
Content-Length: {}
Location: http://127.0.0.1

'''

text = '<!DOCTYPE html><html><body>Hello world</body></html>'


def generate_response(code, code_descr, text):
    text = text.encode('utf-8')
    now = datetime.now()
    response = headers.format(code, code_descr, now.hour - 3, now.minute, now.second, len(text)).encode('utf-8') + text
    return response


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

server.bind(('127.0.0.1', 5000))
server.listen()

while True:
    client_socket, addr = server.accept()
    print(client_socket, addr)
    request = client_socket.recv(4096).decode('utf-8')
    print(request)
    method, resource, *other = request.split()
    if resource == '/admin':
        response = generate_response(403, 'Forbidden', '<!DOCTYPE html><html><body>Forbidden</body></html>')
    elif resource == '/':
        response = generate_response(200, 'OK', text)
    else:
        response = generate_response(404, 'Not Found', '<!DOCTYPE html><html><body>Not found</body></html>')
    client_socket.sendall(response)
