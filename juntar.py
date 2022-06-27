from itertools import combinations
from PIL import Image
import os
import random

#repeat for all pictures
for i in range(500):
    img1 = Image.open('D:\\randomPictures\\images\\image' + str(random.randint(1,49)) + '.png')
    img2 = Image.open('D:\\randomPictures\\images2\\image' + str(random.randint(1,49)) + '.png')
    img3 = Image.open('D:\\randomPictures\\images3\\image' + str(random.randint(1,49)) + '.png')
    img4 = Image.open('D:\\randomPictures\\images4\\image' + str(random.randint(1,49)) + '.png')
    img5 = Image.open('D:\\randomPictures\\images5\\image' + str(random.randint(1,49)) + '.png')

    ran1 = random.choices ([img1, img2, img3, img4, img5], weights=[0.2, 0.2, 0.2, 0.2, 0.2])
    ran2 = random.choices ([img1, img2, img3, img4, img5], weights=[0.2, 0.2, 0.2, 0.2, 0.2])

    #generate unique combinations of images to avoid repetition

    if (ran1 != ran2):
        combine = Image.blend(ran1[0], ran2[0], 0.5)
        combine.save('D:\\randomPictures\\combined\\combined' + str(i) + '.png')



    