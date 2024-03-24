#Фильтрация изображения на основе ДКП для всей картинки

import numpy as np
from PIL import Image

A = np.zeros((256, 256), "float32")     #Реализация матрицы ДКП
for i in range(256):
    for j in range(256):
        A[i][j] = np.cos(np.pi*(2*i+1)*j/512) #Здесь надо помнить про теорему Котельникова
At = np.transpose(A)


path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaNoised.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256)

res = np.dot(A, np.dot(img, At))        #Перешел в частотную область
for i in range(256):                    #Убрал высокочастотные коэффициенты
    for j in range(256):
        if (i**2 + j**2)**0.5 > 155:
            res[i][j] = 0
res = np.dot(np.linalg.inv(A), np.dot(res, np.linalg.inv(At))) #Перешел в пространственную область

for i in range(256):
    for j in range(256):
        res[i][j] = round(res[i][j])
        if res[i][j] > 255:
            res[i][j] = 255
        if res[i][j] < 0:
            res[i][j] = 0

res = Image.fromarray(res.astype("uint8"), "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaDCTDenoised.jpg")

