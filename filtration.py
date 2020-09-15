import cv2 as cv
import numpy as np
import math

class Filtration:
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

    def normalize(self, v):
        if v < 0:
            v = 0
        elif v > 255:
            v = 255

        return v

    def stdFiltration(self, mask):
        image_out = np.zeros((self.getHeight(), self.getWidth(), self.getChannel()), np.uint8)
        enlarged = np.zeros((self.getHeight() + mask, self.getWidth() + mask, self.getChannel()), np.uint8)

        for i in range(mask, self.getWidth()):
            for j in range(mask, self.getHeight()):
                enlarged[j,i] = self.image_in[j,i]

        for i in range(mask, self.getWidth()):
            for j in range(mask, self.getHeight()):

                stdR = 0 
                stdG = 0
                stdB = 0
                s = math.floor(mask/2)

                for k in range(-s, s):
                    for z in range(-s, s):
                        R = int(enlarged[j + z, i + k, 0])
                        G = int(enlarged[j + z, i + k, 1])
                        B = int(enlarged[j + z, i + k, 2])

                        stdR += (R - int(enlarged[j, i, 0])) * (R - int(enlarged[j, i, 0]))
                        stdG += (G - int(enlarged[j, i, 1])) * (G - int(enlarged[j, i, 1]))
                        stdB += (B - int(enlarged[j, i, 2])) * (B - int(enlarged[j, i, 2]))

                stdR /= 3 * 3 - 1
                stdG /= 3 * 3 - 1
                stdB /= 3 * 3 - 1

                stdR = self.normalize(stdR)
                stdG = self.normalize(stdG)
                stdB = self.normalize(stdB)

                image_out[j, i, 0] = stdR
                image_out[j, i, 1] = stdG
                image_out[j, i, 2] = stdB

        return image_out

        
        