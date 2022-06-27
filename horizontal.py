import random
import math
from tracemalloc import stop
from samila import *
import os
import json

a = random.random()
b = random.random()

x = random.random() * math.e
y = random.random() * math.pi

seeds = []
if not os.path.exists("images3"):
    os.mkdir(os.getcwd() + "\\images3")

def f1(x,y):
    return random.uniform(-1,1) - math.atan2(x,y)
    
def f2(x,y):
    return  random.uniform(-5,5) - math.cos(y) * math.pi

#save img multiple times
for i in range(50):
    g = GenerativeImage(f1, f2)
    g.generate()

    #add unique seeds to the list
    seed = g.seed
    if seed not in seeds:
        seeds.append(seeds)
        g.plot(projection=Projection.RANDOM , color= random.choice(seq=['red', 'yellow', 'white', 'orange', 'pink', 'cyan']), bgcolor='black')
        g.save_image(os.getcwd()+'\\images3\image' + str(i) + '.png')

    #save the seeds to a json file
with open('horizontal_seeds.json', 'w') as outfile:
    json.dump(seeds, outfile)
    