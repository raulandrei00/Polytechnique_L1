import telnetlib

host = "127.0.0.1"
port = 8888

with telnetlib.Telnet(host, port) as tn:
    tn.write(b"Hello, server!\n")
    response = tn.read_all()
    print(response.decode())