from itertools import combinations
from PIL import Image
import os
import random

if not os.path.exists("combined"):
    os.mkdir(os.getcwd() + "\\combined")

#repeat for all pictures
for i in range(100):
    img1 = Image.open(os.getcwd()+'\\images\\image' + str(random.randint(1,49)) + '.png').convert('RGBA')
    img2 = Image.open(os.getcwd()+'\\images2\\image' + str(random.randint(1,49)) + '.png').convert('RGBA')
    img3 = Image.open(os.getcwd()+'\\images3\\image' + str(random.randint(1,49)) + '.png').convert('RGBA')
    img4 = Image.open(os.getcwd()+'\\images4\\image' + str(random.randint(1,49)) + '.png').convert('RGBA')
    img5 = Image.open(os.getcwd()+'\\images5\\image' + str(random.randint(1,49)) + '.png').convert('RGBA')

    ran1 = random.choices ([img1, img2, img3, img4, img5], weights=[0.2, 0.2, 0.2, 0.2, 0.2])
    ran2 = random.choices ([img1, img2, img3, img4, img5], weights=[0.2, 0.2, 0.2, 0.2, 0.2])

    #generate unique combinations of images to avoid repetition

    if (ran1 != ran2):
        combine = Image.blend(ran1[0], ran2[0], 0.5)
        combine.save(os.getcwd()+'\\combined\\nft' + str(i) + '.png')



    