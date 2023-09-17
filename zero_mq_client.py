import sys
import zmq
import cv2
import numpy as np
from flood import flood
from edgeDetector import edgeDetector

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)


socket.connect("tcp://127.0.1.1:5556")
socket.setsockopt(zmq.SUBSCRIBE,b'')
socket.setsockopt(zmq.CONFLATE, 1)

# Process 5 updates
total_temp = 0


while True:
    received_bytes = socket.recv()
    #print(received_bytes)
    np_array = np.frombuffer(received_bytes, dtype=np.uint8)
    image = cv2.imdecode(np_array,1)
    edgeDetector(image)
    # result,left,right = flood(image)
    # cv2.imshow('floor finder',result)
    cv2.imshow('image',image)
    cv2.waitKey(1)