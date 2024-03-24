#Реализация ДСП для всего изображения, код просто перегоняет массив из пространственной области в частотную и обратно
#На первый взгляд может показаться, что никаких изменений быть не должно, но это не так

import numpy as np
from PIL import Image

A = np.zeros((256, 256), "float32")
for i in range(256):
    for j in range(256):
        A[i][j] = np.sin(np.pi*(2*i+1)*j/512)

At = np.transpose(A)


path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaGray.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256)

res = np.dot(A, np.dot(img, At))
res = np.dot(np.linalg.pinv(A), np.dot(res, np.linalg.pinv(At)))

for i in range(256):
    for j in range(256):
        res[i][j] = round(res[i][j])
        if res[i][j] > 255:
            res[i][j] = 255
        if res[i][j] < 0:
            res[i][j] = 0

res = Image.fromarray(res.astype("uint8"), "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaDST.jpg")