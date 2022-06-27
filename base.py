import random
import math
from tracemalloc import stop
from samila import *

a = random.random()
b = random.random()

x = random.random() * math.e
y = random.random() * math.pi

def f1(x,y):
    return random.uniform(-1,1) * x * math.e  - math.sin(y**2)
    
def f2(x,y):
    return  random.gauss(a,b) * y * random.random() - math.cos(x**2) 

#save img multiple times
for i in range(50):
    g = GenerativeImage(f1, f2)
    g.generate()
    g.plot(projection=Projection.RANDOM , color= random.choice(seq=['red', 'yellow', 'white', 'orange', 'pink', 'cyan']), bgcolor='black')
    g.save_image('D:\\randomPictures\\images\\image' + str(i) + '.png')