#Наивная фильтрация Винера (Считается, что спектры зашумленного изображения и исходного примерно равны)
#При большой зашумленности, спектры начинают сильно отличаться, поэтому фильтр начинает хуже работать 
#Для сравнения прикреплены изображения "IdealWiener", где в качестве опорного спектра использовался спектр оригинального изображения 
#И "RealWiener", где использовался спектр только зашумленного изображения

import numpy as np
from PIL import Image

path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaNoised.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256)


A = np.zeros((256, 256), "float32")     #Реализация матрицы ДКП
for i in range(256):
    for j in range(256):
        A[i][j] = np.cos(np.pi*(2*i+1)*j/512)
At = np.transpose(A)


img = np.dot(A, np.dot(img, At))     #Перешел в частотную область
for i in range(256):
    for j in range(256):
        img[i][j] = (img[i][j]**2/(img[i][j]**2 + 72*256*256))*img[i][j]     #Фильтрация Винера

res = np.dot(np.linalg.inv(A), np.dot(img, np.linalg.inv(At)))      #Перешел в пространственную область
res = Image.fromarray(res.astype("uint8"), "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/Wiener.jpg")