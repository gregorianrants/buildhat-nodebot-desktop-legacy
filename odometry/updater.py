import time
import math

DISTANCE_BETWEEN_WHEELS = 176

class Updater:
    def __init__(self):
        self.theta = 0
        self.x = 0
        self.y = 0
        self.Vl = 0
        self.Vr = 0
        self.V = 0
        self.previousTime = None
        
        
    def updateLeft(self,speed):
        self.Vl = speed
        self.V = self.Vl
        
        currentTime = time.perf_counter()
       
        if self.Vr and self.previousTime:
            #print('time',currentTime-self.previousTime)
            dt = currentTime - self.previousTime
            print(dt)
            Vtheta = (self.Vr-self.Vl)/DISTANCE_BETWEEN_WHEELS
            self.theta = self.theta + Vtheta*dt
            self.x = self.x + self.V*dt*math.cos(self.theta)
            self.y = self.y + self.V*dt*math.sin(self.theta)
            
            print('theta',self.theta)
        self.previousTime = currentTime
        
    def updateRight(self,speed):
        self.Vr = speed

