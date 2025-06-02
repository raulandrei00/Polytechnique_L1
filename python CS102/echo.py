# --------------------------------------------------------------------
import asyncio
import sys
from typing import cast

# --------------------------------------------------------------------
class EchoServerClientProtocol(asyncio.Protocol):

    def __init__(self):
        self.transport : asyncio.Transport = None
        self.buffer : bytes = b''

    def connection_made(self, transport : asyncio.BaseTransport) -> None:
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = cast(asyncio.Transport, transport)



    def data_received(self, data : bytes) -> None:
        # convert the binary data received into a string
        message : str = data.decode()
        print('Data received: {!r}'.format(message))

        # send the same data back
        # print('Send: {!r}'.format(message))

        # convert message to uppercase
        message_send = message.upper()
        data_send = message_send.encode()

        self.buffer += data_send
        print('Send: {!r}'.format(data_send))

        if message_send[-1] == '\n':
            self.transport.write(self.buffer)
            print('Send: {!r}'.format(data_send))
            if "CLOSE" in self.buffer.decode():
                print('Close the client socket')
                self.transport.close()
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

coro   = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
server : asyncio.base_events.Server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass