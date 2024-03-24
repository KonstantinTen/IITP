#Удаление шума усредняющим фильтром

import numpy as np
from PIL import Image

path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaNoised.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256)    #изображение стало массивом

kernel = np.array([[1/16, 1/8, 1/16],       #усредняющие ядро свертки
                   [1/8, 1/4, 1/8],
                   [1/16, 1/8, 1/16]])

res = np.zeros((254, 254))
for i in range(254):                #Сама свертка
    for j in range(254):
        res[i][j] = np.sum(np.multiply(img[i:i+3, j:j+3], kernel))

res = Image.fromarray(res.astype("uint8"), "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaAverDenoised.jpg")