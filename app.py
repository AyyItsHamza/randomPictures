import random
import math
import matplotlib as mpl
from samila import *

a = random.uniform(random.random() , random.random() )
b = random.uniform(random.random() , random.random() )

x = random.random() * math.pi
y = random.random() * math.pi
op = random.choice(seq=(['+', '-']))

def f1(x,y):
    #result = random.uniform(a,b) * x**2 , op , random.random() , op , math.sin(y**2) , op , math.cos(random.random() * math.pi)
    #return result
    return random.uniform(a,b) * random.random() - random.random() - math.sin(y**2) - math.cos(random.random() * math.pi)

def f2(x,y):
    #result = random.uniform(a,b) * y**3 , op , random.random() , op , math.cos(x**2) / 2
    return  random.uniform(a,b) * y**3 + random.random() - math.cos(x**2) / 2
    #return result

#save img multiple times
for i in range(10):
    g = GenerativeImage(f1, f2)
    g.generate()
    g.plot(projection=Projection.RANDOM , color= random.choice(seq=['red', 'green', 'yellow', 'white', 'purple', 'orange', 'pink', 'cyan']), bgcolor='black')
    g.save_image('image' + str(i) + '.png')