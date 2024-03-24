#Код зашумляющий изображение аддитивным Гауссовским шумом

import numpy as np
from PIL import Image


path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaGray.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256) #изображение стало массивом
noise = np.random.normal(0, 20, (256, 256)) #Генерация шума, первый параметр (0) - мат.ожидание, второй (20) - дисперсия
res = img + noise

for i in range(256):                    #Не даю вылезти за границы дозволеного
    for j in range(256):
        res[i][j] = round(res[i][j])
        if res[i][j] > 255:
            res[i][j] = 255
        if res[i][j] < 0:
            res[i][j] = 0

res = Image.fromarray(res.astype("uint8"), "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaAddNoise.jpg")
