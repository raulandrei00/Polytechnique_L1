# --------------------------------------------------------------------
import asyncio
import sys

# --------------------------------------------------------------------
class ChatServerState:
    def __init__ (self):
        self.clients = []  # List of connected clients
        self.client_by_nickname = dict()

# --------------------------------------------------------------------
class ChatServerClientProtocol(asyncio.Protocol):
    def __init__(self, state : ChatServerState):
        self.state = state
        self.buffer : bytes = b''
        
        

    def connection_made(self, transport : asyncio.BaseTransport) -> None:
        # register the client in self.state
        
        self.transport = transport
        self.nickname = None
        self.state.clients.append(transport)  # Add the transport to the global state
        
        print(f"Client connected: {transport.get_extra_info('peername')}")
        print("HERE " , self.state.clients)
        # note that `transport` can be used as a key in a dictionary
        

    def connection_lost(self, exc : Exception | None) -> None:
        self.state.clients.remove(self.transport)  # Remove the transport from the global state
        print(f"Client disconnected: {self.transport.get_extra_info('peername')}")

    def data_received(self, data : bytes) -> None:
        # buffer the received data until a full line is received
        # then, forward that full line to all clients
        message : str = data.decode()
        print(f"Data received: {message!r}")
        # send the same data back to all clients
        
        data_send = message.encode()

        self.buffer += data_send
        # print('Send: {!r}'.format(data_send))

        if message[-1] == '\n':
            if self.nickname is None:
                # if the nickname is not set, set it to the first word of the message
                self.nickname = self.buffer.decode()[:-2]
                # remove the last two characters (the newline and the space)
                print(f"Nickname set to: {self.nickname}")
                self.buffer = f"{self.nickname} has joined the chat\n".encode()
                self.state.client_by_nickname[self.nickname] = self.transport
                print(self.state.client_by_nickname)

            if self.buffer.decode().startswith("#"):
                recipient = self.buffer.decode().split(" ")[0][1:]
                message = self.buffer.decode().split(" ", 1)[1]
                print(f"Sending private message to {recipient}: {message}")
                self.state.client_by_nickname[recipient].write(f"{self.nickname}: {message}".encode())
            if self.buffer.decode() == "!users\r\n":
                print(f"Sending users list to {self.nickname}")
                users = ", ".join(self.state.client_by_nickname.keys())
                self.transport.write(f"Connected users: {users}\n".encode())

            for client in self.state.clients:
                if client == self.transport:
                    continue
                print(f"Sending to client: {client.get_extra_info('peername')}")
                # if client != self.transport:
                client.write(f"{self.nickname}: {self.buffer.decode()}".encode())
                    
                
            print('Send: {!r}'.format(self.buffer))
            
            self.buffer = b''
        
# --------------------------------------------------------------------
if sys.version_info < (3, 10):
    loop = asyncio.get_event_loop()
else:
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)

state = ChatServerState()

def create_protocol() -> ChatServerClientProtocol:
    global state
    return ChatServerClientProtocol(state)

coro   = loop.create_server(create_protocol, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass