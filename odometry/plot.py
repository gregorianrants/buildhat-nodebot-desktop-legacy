import matplotlib.pyplot as plt
import numpy as np
import time


class Plot:
    def __init__(self):
        self.origin_robot = np.array([[0,0],[0,80],[150,80],[150,0],[0,0]]).T
        self.orign_nose = np.array([[150],[40]])
        self.robot = self.origin_robot.copy()
        self.nose = self.orign_nose.copy()
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-500,2500)
        self.ax.set_ylim(-500,3500)
        self.ax.set_aspect('equal')
        x = self.robot[0,:]
        y = self.robot[1,:]
        self.line, = self.ax.plot(x,y)
        # self.dots = self.ax.scatter(self.orign_nose[0,0],self.orign_nose[1,0])
        self.dots = self.ax.scatter(self.nose[0],self.nose[1],c='red')
        
        self.translation = np.array([[0],[0]])
        self.rotation = 0
        
    def setTranslation(self,vec):
        self.translation = vec
        self.updateRobot()
        self.updatePlot()
        
    def setRotation(self,theta):
        self.rotation = theta
        self.updateRobot()
        self.updatePlot()
        
    def updateRobot(self):
        theta = self.rotation
        rotationMatrix = np.array([
            [np.cos(theta),-np.sin(theta)],
            [np.sin(theta),np.cos(theta)]
            ])
        rotated = rotationMatrix @ self.origin_robot
        rotated_nose = rotationMatrix @ self.orign_nose
        self.robot = rotated + self.translation
        self.nose = rotated_nose + self.translation
    
    def updatePlot(self):
        x = self.robot[0,:]
        y = self.robot[1,:]
        self.line.set_ydata(y)
        self.line.set_xdata(x)
        self.dots.set_offsets([[self.nose[0],self.nose[1]]])
    
        # drawing updated values
        self.fig.canvas.draw()
 
        # This will run the GUI event
        # loop until all UI events
        # currently waiting have been processed
        self.fig.canvas.flush_events()
        



# plot = Plot()
# plot.updatePlot()




# while True:
#     plot.setTranslation(np.array([[400],[400]]))
#     plot.setRotation((np.pi/2)/2)
#     time.sleep(3)
    



