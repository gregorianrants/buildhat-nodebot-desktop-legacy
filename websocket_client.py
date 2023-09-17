import asyncio
from websockets.client import connect
import numpy as np
import cv2
import io
from PIL import Image
from flood import flood

async def main():
    buffer = b''
    async with connect('ws://192.168.178.52:3000') as websocket:
        async for message in websocket:
            #message = bytes.fromhex(message)
            index = message.find(bytes.fromhex('ffd9'))
            if index == -1:
                buffer += message
            else:
                index_after_last_byte = index + 2
                #print(message[index_after_last_byte-10:index_after_last_byte].hex())
                result = buffer+message[:index_after_last_byte]
                #print('result',result[-10:].hex())
                if len(message)>index_after_last_byte:
                    buffer = message[index_after_last_byte:]
                else:
                    buffer = b''
                image = Image.open(io.BytesIO(result))
                image_np = np.array(image)
                image_np,left,right = flood(image_np)
                image_bgr = cv2.cvtColor(image_np,cv2.COLOR_BGR2RGB)
                #print(image_bgr.shape)
                # image = np.frombuffer(decoded,dtype='uint8').reshape((480,640,3))
                cv2.imshow('image', image_bgr)
                cv2.waitKey(1)



try:
    asyncio.run(main())
    cv2.waitKey(0)
except KeyboardInterrupt:
    exit()
