import random
import math
from tracemalloc import stop
from samila import *
import os

a = random.random()
b = random.random()

x = random.random() * math.e
y = random.random() * math.pi

seeds = []
if not os.path.exists("images2"):
    os.mkdir(os.getcwd() + "\\images2")

def f1(x,y):
    return random.uniform(-1,1) - math.atan2(x,y)
    
def f2(x,y):
    return  random.gauss(5,5) - math.atan2(x,y) * math.tau

#save img multiple times
for i in range(50):
    g = GenerativeImage(f1, f2)
    g.generate()

    #add unique seeds to the list
    seed = g.seed
    if seed not in seeds:
        seeds.append(seeds)
        g.plot(projection=Projection.RANDOM , color= random.choice(seq=['red', 'yellow', 'white', 'orange', 'pink', 'cyan']), bgcolor='black')
        g.save_image(os.getcwd()+'\\images2\\image' + str(i) + '.png')
