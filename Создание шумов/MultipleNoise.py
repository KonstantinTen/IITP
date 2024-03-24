#Код зашумляющий изображение мультипликативным Гауссовским шумом

import numpy as np
from PIL import Image


path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaGray.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256) #изображение стало массивом
noise = np.random.normal(1, 0.08, (256, 256))            #Генерация шума, первый параметр (1) - мат.ожидание, второй (0.08) - дисперсия
res = np.multiply(img, noise).astype("uint8")

for i in range(256):                #Не даю вылезти за границы дозволеного
    for j in range(256):
        res[i][j] = round(res[i][j])
        if res[i][j] > 255:
            res[i][j] = 255
        if res[i][j] < 0:
            res[i][j] = 0

res = Image.fromarray(res, "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaMultNoise.jpg")