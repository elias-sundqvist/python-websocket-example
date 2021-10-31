import _thread
import logging
from websocket_server import WebsocketServer
import http.server
import socketserver
import json 
import api

IP = '127.0.0.1'
WS_PORT = 1655
HTTP_PORT = 8000

server = WebsocketServer(host=IP, port=WS_PORT, loglevel=logging.INFO)

def message_received(client, server, message):
    data = json.loads(message)
    result = getattr(api, data['func'])(*data['args'])
    print(f"Message Recieved '{message}'")
    response = json.dumps({'id':data['id'], 'res':result})
    print(f"Responding with '{response}'")
    server.send_message_to_all(response)

server.set_fn_message_received(message_received)
_thread.start_new_thread(server.run_forever, ())


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)


with socketserver.TCPServer(("", HTTP_PORT), Handler) as httpd:
    print(f"Serving website on http://{IP}:{HTTP_PORT}/")
    httpd.serve_forever()
