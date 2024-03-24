#Код зашумляющий изображение импульсным шумом

import random
import numpy as np
from PIL import Image


path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaGray.jpg"  #путь до изображения
img = Image.open(path)
res = np.array(img.getdata(), "uint8").reshape(256, 256)

for k in range(4096):           #Выбираю где-то 1/16 от всех точек (точки могут совпасть)
    i = random.randint(0, 256)  #Точки случайные, ибо координаты случайные
    j = random.randint(0, 256)
    p = random.randint(0, 8)/4  #Случайно выбираю тип: "соль" или "перец"
    if p < 1:
        res[i][j] = 0
    else:
        res[i][j] = 255

res = Image.fromarray(res, "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaImpulseNoise.jpg")