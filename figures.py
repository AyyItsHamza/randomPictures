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

if not os.path.exists("images5"):
    os.mkdir(os.getcwd() + "\\images5")

def f1(x,y):
    return random.uniform(a,b) - math.ceil(y)
    
def f2(x,y):
    return  random.uniform(a,b) - math.copysign(math.cos(x),y) * math.pi 

#save img multiple times
for i in range(50):
    g = GenerativeImage(f1, f2)
    g.generate()

    seed = g.seed
    if seed not in seeds:
        seeds.append(seed)
        g.plot(projection=Projection.RANDOM , color= random.choice(seq=['red', 'yellow', 'white', 'orange', 'pink', 'cyan']), bgcolor='black')
        g.save_image(os.getcwd()+'\\images5\\image' + str(i) + '.png')

#save the seeds to a json file
with open('figures_seeds.json', 'w') as outfile:
    json.dump(seeds, outfile)