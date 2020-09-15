import cv2 as cv
import argparse
import affine_transformation as aft
import morphological_gradient as mg
import filtration as ft
import logic as l
import numpy as np

parser = argparse.ArgumentParser(description='Code for Affine Transformations tutorial.')
parser.add_argument('--input', help='Path to input image.', default='F_dzieciol.png')
parser.add_argument('--logic', help='Path to logical image.', default='kropken.png')
args = parser.parse_args()

image_in = cv.imread(cv.samples.findFile(args.input))
image_log = cv.imread(cv.samples.findFile(args.logic),0)

if image_in is None:
    print('Could not open or find the image:', args.input)
    exit(0)

try:
    operation = int(input("""
            Affine Transformation:
                1 - Translate
                2 - Scale
                3 - Rotate
                4 - Lean
                5 - Matrix
            6 - Standard Deviation Filtration
            7 - Morphological Gradient (image - erode)
            8 - Morphological Gradient (dilate - image)
            9 - Morphological Gradient (dilate - erode)/2
            0 - Logic\n
            Choose operation: """))

except:
    print('Integer is required!')
    exit(0)

def translate():
    at = aft.affineTransformation(image_in)
    x = int(input('Podaj x: '))
    y = int(input('Podaj y: '))
    image_out = at.translate(y,x)
    cv.imwrite('output/translate.png', image_out)

def scale():
    at = aft.affineTransformation(image_in)
    x = int(input('Podaj x: '))
    y = int(input('Podaj y: '))
    image_out = at.scale(y,x)
    cv.imwrite('output/scale.png', image_out)

def rotate():
    at = aft.affineTransformation(image_in)
    x = int(input('Podaj kat: '))
    image_out = at.rotate(x)
    cv.imwrite('output/rotate.png', image_out)

def lean():
    at = aft.affineTransformation(image_in)
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    image_out = at.lean(b,a)
    cv.imwrite('output/lean.png', image_out)

def matrix():
    at = aft.affineTransformation(image_in)
    print('Podaj macierz: (kolejnosc [ 1 2; 3 4; 5 6 ]')
    m = [[0,0], [0,0], [0,0]]
    for i in range(3):
        for j in range(2):
            m[i][j] = float(input())
    image_out = at.matrix(m)
    cv.imwrite('output/matrix.png', image_out)

def stdfiltration():
    filtration = ft.Filtration(image_in)
    m = int(input('Podaj maske: '))
    image_out = filtration.stdFiltration(m)
    cv.imwrite('output/filtration.png', image_out)

def gradient1():
    gradient = mg.morphologicalGradient(image_in)
    image_out = gradient.gradient1()
    cv.imwrite('output/gradient1.png', image_out)

def gradient2():
    gradient = mg.morphologicalGradient(image_in)
    image_out = gradient.gradient1()
    cv.imwrite('output/gradient2.png', image_out)

def gradient3():
    gradient = mg.morphologicalGradient(image_in)
    image_out = gradient.gradient3()
    cv.imwrite('output/gradient3.png', image_out)

def logic():
    logic = l.Logic(image_log)
    image_out = logic.edgeIntersection()
    cv.imwrite('output/logic.png', image_out*255)

def image_transformation(operation):
    switcher = {
        1: translate,
        2: scale,
        3: rotate,
        4: lean,
        5: matrix,
        6: stdfiltration,
        7: gradient1,
        8: gradient2,
        9: gradient3,
        0: logic
    }
    func=switcher.get(operation, lambda :print('\n===!Invalid operation!===\n'))
    return func()

image_transformation(operation)

#for i in range(0,10):
#    image_transformation(i)



#image_out = cv.cvtColor(image_out, cv.COLOR_BGR2RGB)
#cv.imshow('Source image', image_out * 255)
# cv.imwrite('output/logic.png', image_out*255)
#cv.waitKey()

