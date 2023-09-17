import zmq
from operator import itemgetter
import json
from updater import Updater
from plot import Plot
import numpy as np

updater = Updater()
plot = Plot()

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://192.168.178.52:3000")
socket.setsockopt(zmq.SUBSCRIBE,b'')
##socket.setsockopt(zmq.CONFLATE, 1)

print('ready')

for i in range(40000):
    json_bytes = socket.recv()
    as_dict = json.loads(str(json_bytes,encoding='utf-8'))
    side,speed = itemgetter('side','speed')(as_dict)
    
    if(side=='left'):
        updater.updateLeft(speed)
        print(updater.x)
        print(updater.y)
        if(i%100==0):
            print(updater.x)
            print(updater.y)
            translationVector = np.array([[updater.x],[updater.y]])
            theta = updater.theta
            plot.setRotation(theta)
            plot.setTranslation(translationVector)
    else:
        updater.updateRight(speed)
        if(i%100==0):
            translationVector = np.array([[updater.x],[updater.y]])
            theta = updater.theta
            plot.setRotation(theta)
            plot.setTranslation(translationVector)
    
    
    