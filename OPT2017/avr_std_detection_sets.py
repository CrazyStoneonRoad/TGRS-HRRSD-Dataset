# This file is used to compute average and standard deviation
# for object detection datasets.
#
# Put this file under root of the datasets, where there is a
# JPEGImages folder containing images.

import os, math, sys
# from PIL import Image as IMG
# import numpy.random as RAN
import random
import numpy as np
#from scipy.misc import imread
from imageio import imread
from tqdm import tqdm

def avr(p, im_id):
    pth = os.path.join(p, im_id)
    im = imread(pth)
    n = im.shape[0] * im.shape[1]

    avr = np.sum(np.sum(im,0),0)/n
    return avr


def std2(p, im_id, avr):
    pth = os.path.join(p, im_id)
    im = imread(pth)
    n = im.shape[0] * im.shape[1]

    minus = np.subtract(im, avr)
    minus2 = np.power(minus,2)
    std2 = np.sum( np.sum(minus2,0),0 )/n
    return std2

N = int(sys.argv[2])  # 500
path_img = sys.argv[1] # 'JPEGImages/'
AVR = [0,0,0]
STD2 = [0,0,0]

list_im = os.listdir(path_img) 
list_im_ = random.sample(list_im,N)
count = 0
for i in tqdm(list_im_):
    count=count+1
    avr__ = avr(path_img, i)
    AVR = [avr__[i]+AVR[i] for i in range(3)]
    pass
AVR = [AVR[i]/N for i in range(3)]
print( 'AVR:\n', AVR)

count = 0
for i in tqdm(list_im_):
    count=count+1
    std2__ = std2(path_img, i,AVR)
    STD2 = [std2__[i]+STD2[i] for i in range(3)]
    pass
STD2 = [STD2[i]/N for i in range(3)]
STD = [math.sqrt(STD2[i]) for i in range(3)]
print( '\nSTD:\n', STD )
