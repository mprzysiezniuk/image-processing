#from __future__ import print_function
import cv2 as cv
import numpy as np
import math as m

class affineTransformation:

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

    def matrix(self, m):
        h_out = int(self.getHeight() * m[1][1] + abs(m[0][1]) * self.getWidth() + m[2][1])
        w_out = int(self.getWidth() * m[0][0] + abs(m[1][0]) * self.getHeight() + m[2][0])

        image_out = np.zeros((h_out + 1, w_out + 1, self.getChannel()), np.uint8)

        for y0 in range(self.getHeight()):
            for x0 in range(self.getWidth()):
                y = int(x0 * m[0][1] + y0 * m[1][1] + m[2][1])
                x = int(x0 * m[0][0] + y0 * m[1][0] + m[2][0])

                if 0 < y < h_out and 0 < x < w_out:
                    image_out[y,x] = self.image_in[y0,x0]
                    image_out[y + 1,x] = self.image_in[y0,x0]
                    image_out[y,x + 1] = self.image_in[y0,x0]
                    image_out[y + 1,x + 1] = self.image_in[y0,x0]

        return image_out

#====================================================================

    def translate(self, h, w):
        h_out = self.getHeight()+h
        w_out = self.getWidth()+w
        image_out = np.zeros((h_out, w_out, self.getChannel()), np.uint8)

        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                image_out[y+h, x+w] = self.image_in[y,x]

        return image_out

#====================================================================

    def scale(self, a, b):
        h_out = int(self.getHeight() * a)
        w_out = int(self.getWidth() * b)
        image_out = np.zeros((h_out, w_out, self.getChannel()), np.uint8)

        for y in range(h_out):
            for x in range(w_out):
                if 0 < y < h_out and 0 < x < w_out:
                    image_out[y,x] = self.image_in[int(y/a), int(x/b)]

        return image_out

#====================================================================

    def rotate(self, angle):
        
        angle_rad = m.radians(angle)
        cs = m.cos(angle_rad)
        ss = m.sin(angle_rad)

        ssx = m.sin(m.pi/2 - angle_rad)
        ss90 = m.sin(m.pi/2)

        w = int(ss * self.getHeight()/ss90 + ssx * self.getWidth()/ss90)
        h = int(ssx * self.getHeight()/ss90 + ss * self.getWidth()/ss90)

        image_out = np.zeros((h + 1, w + 1, self.getChannel()), np.uint8)

        y0 = self.getHeight() / 2
        x0 = self.getWidth() / 2
        
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                posx = int(round( cs * (x - x0) - ss * (y - y0) + w/2))
                posy = int(round( ss * (x - x0) + cs * (y - y0) + h/2))

                if 0 < posx < w and 0 < posy < h:
                    image_out[posy, posx] = self.image_in[y, x]

                    image_out[posy + 1, posx] = self.image_in[y, x]
                    image_out[posy, posx + 1] = self.image_in[y, x]
                    image_out[posy + 1, posx + 1] = self.image_in[y, x]
        
        return image_out


#====================================================================

    def lean(self, a, b):
        h_out = int(self.getHeight() + a * self.getWidth())
        w_out = int(self.getWidth() + b * self.getHeight())
        image_out = np.zeros((h_out, w_out, self.getChannel()), np.uint8)

        for y0 in range(self.getHeight()):
            for x0 in range(self.getWidth()):
                y = int(y0 + a*x0)
                x = int(x0 + b*y0)
                if 0 < y < h_out and 0 < x < w_out:
                    image_out[y,x] = self.image_in[y0,x0]

        return image_out


