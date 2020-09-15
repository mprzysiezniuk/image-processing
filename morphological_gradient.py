import cv2 as cv
import numpy as np
import math

class morphologicalGradient:
    def __init__(self, image_in):
        self.image_in = image_in
        self.height, self.width, self.channel = self.image_in.shape

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width
    
    def getChannel(self):
        return self.channel

#====================================================================

    def erode(self):
        image_out = np.zeros_like(self.image_in)
        SE = np.array([[0, 1, 0],[1, 1, 1], [0, 1, 0]])
        
        for y in range(1, self.getHeight()-1):
            for x in range(1, self.getWidth()-1):
                
                if self.getChannel() == 3:
                    arr = self.image_in[y-1:y+2, x-1:x+2, :]
                    bool_idx = (SE == 1)
                    image_out[y,x,0] = min(arr[bool_idx, 0])
                    image_out[y,x,1] = min(arr[bool_idx, 1])
                    image_out[y,x,2] = min(arr[bool_idx, 2])
                
                elif self.getChannel() == 1:
                    bool_idx = (SE == 1)
                    arr = self.image_in[y-1:y+2, x-1:x+2]
                    image_out[y,x] = min(arr[bool_idx])
        
        return image_out

    def dilate(self):
        image_out = np.zeros_like(self.image_in)
        SE = np.array([[0, 1, 0],[1, 1, 1], [0, 1, 0]])
        
        for y in range(1, self.getHeight()-1):
            for x in range(1, self.getWidth()-1):
                
                if self.getChannel() == 3:
                    arr = self.image_in[y-1:y+2, x-1:x+2, :]
                    bool_idx = (SE == 1)
                    image_out[y,x,0] = max(arr[bool_idx, 0])
                    image_out[y,x,1] = max(arr[bool_idx, 1])
                    image_out[y,x,2] = max(arr[bool_idx, 2])
                
                elif self.getChannel() == 1:
                    bool_idx = (SE == 1)
                    arr = self.image_in[y-1:y+2, x-1:x+2]
                    image_out[y,x] = max(arr[bool_idx])
        
        return image_out

#====================================================================

    def gradient1(self):
        image_out = np.zeros((self.getHeight(), self.getWidth(), self.getChannel()), np.uint8)
        image_out = self.image_in - self.erode()

        return image_out

    def gradient2(self):
        image_out = np.zeros((self.getHeight(), self.getWidth(), self.getChannel()), np.uint8)
        image_out = self.dilate() - self.image_in

        return image_out

    def gradient3(self):
        image_out = np.zeros((self.getHeight(), self.getWidth(), self.getChannel()), np.uint8)
        image_out = (self.dilate() - self.erode())/2

        return image_out    