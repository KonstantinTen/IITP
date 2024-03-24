#Фильтрация изображения на основе ДКП для блоков 8x8

import numpy as np
from PIL import Image

A = np.zeros((8, 8), "float32")     #Реализация матрицы ДКП
for i in range(8):
    for j in range(8):
        A[i][j] = np.cos(np.pi*(2*i+1)*j/16)
At = np.transpose(A)


path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaNoised.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256)
res = np.zeros((256, 256))

for i in range(32):             #Пробегаюсь по всем блокам
    for j in range(32):
        block = img[8*i:8*i+8, 8*j:8*j+8]
        block = np.dot(A, np.dot(block, At))    #Перешел в частотную область

        for n in range(8):                      #Убрал высокочастотные коэффициенты
            for m in range(8):
                if (n**2 + m**2)**0.5 > 6.8:
                    block[n][m] = 0

        block = np.dot(np.linalg.inv(A), np.dot(block, np.linalg.inv(At))) #Перешел в пространственную область
        res[8*i:8*i+8, 8*j:8*j+8] = block

for i in range(256):
    for j in range(256):
        res[i][j] = round(res[i][j])
        if res[i][j] > 255:
            res[i][j] = 255
        if res[i][j] < 0:
            res[i][j] = 0

res = Image.fromarray(res.astype("uint8"), "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LocDCTDen.jpg")