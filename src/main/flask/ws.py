from flask import Flask
from flask_sockets import Sockets
from flask_cors import CORS
import json
import sys
import os
import time
import datetime

app=Flask(__name__)
sockets=Sockets(app)

CORS(app, resources={r"/echo": {"origins": "*"}})

@sockets.route('/echo')
def echo_socket(ws):
  while not ws.closed:
    now = datetime.datetime.now().isoformat() + 'Z'
    ws.send(now)
    # msg=input()
    # ws.send(msg)
    time.sleep(1)
    message=ws.receive()
    if message is not None:
      print(message)
    else:
      print('no message')
  if ws.closed:
    print('client closed websocket')

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()

