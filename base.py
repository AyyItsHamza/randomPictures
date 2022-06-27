import random
import math
from tracemalloc import stop
from samila import *
import os
import numpy as np

a = random.random()
b = random.random()

x = random.random() * math.e
y = random.random() * math.pi

seeds = []

if not os.path.exists("images"):
    os.mkdir(os.getcwd() + "\\images")

def f1(x,y):
    return random.uniform(-1,1) * x * math.e  - math.sin(y**2)
    
def f2(x,y):
    return  random.gauss(a,b) * y * random.random() - math.cos(x**2) 

#save img multiple times
for i in range(5):
    g = GenerativeImage(f1, f2)
    g.generate()

    #add unique seeds to the list
    seed = g.seed
    if seed not in seeds:
        seeds.append(seed)
        g.plot(projection=Projection.RANDOM , color= random.choice(seq=['red', 'yellow', 'white', 'orange', 'pink', 'cyan']), bgcolor='black')
        g.save_image(os.getcwd()+'\\images\\image' + str(i) + '.svg')


