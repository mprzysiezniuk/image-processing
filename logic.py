import cv2 as cv
import numpy as np

class Logic:
    def __init__(self, image_in):
        self.image_in = image_in // 255
        self.height, self.width = self.image_in.shape

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

#====================================================================

    def dilate(self, image_in):
        SE = np.array([[1, 1, 1],[1, 1, 1], [1, 1, 1]])
        image_res = np.zeros_like(image_in)
        for y in range(1, self.getHeight()-1):
            for x in range(1, self.getWidth()-1):
                    bool_idx = (SE == 1)
                    arr = image_in[y-1:y+2, x-1:x+2]
                    image_res[y,x] = max(arr[bool_idx])
        
        return image_res

    def conjunction(self, image_out):
        
        return self.image_in & image_out

    def xor(self, image_out):
        
        return np.logical_xor(self.image_in, image_out)

#====================================================================

    def edgeIntersection(self):
        black = np.zeros_like(self.image_in)
        black[:,:] = self.image_in
        black[1:-1, 1:-1] = 0

        comparison_img = black
        dilate = self.dilate(black)
        black = self.conjunction(dilate)
        
        while not np.array_equal(black, comparison_img):
            comparison_img = black
            dilate = self.dilate(black)
            black = self.conjunction(dilate)
        
        black[0,:] = 1
        black[:,0] = 1
        black[-1,:] = 1
        black[:,-1] = 1

        return self.image_in - black
        
        
