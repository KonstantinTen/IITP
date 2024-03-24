#Код зашумляющий изображение аддитивным Гауссовским шумом, коррелирующий с горизонтальной координатой

import numpy as np
from PIL import Image


path = "/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaGray.jpg"  #путь до изображения
img = Image.open(path)
img = np.array(img.getdata(), "uint8").reshape(256, 256) #изображение стало массивом
prenoise = np.random.normal(30, 15, (256, 256)) #Создаю массив случайных значений, мат. ожидание 30, дисперсия 15

for i in range(256):
    prenoise[i] = np.sort(prenoise[i])          #Сортирую

noise = np.zeros((256, 256))

for i in range(256):                            #Формирую шум таким образом, 
    for j in range(128, 256):                   #чтобы в центре отн. горизонтальной оси отклонение было наименьшим, 
        noise[i][j] = prenoise[i][(j-128)*2]    #    а по краям отн. горизонтальной оси отклонение было наибольшим
    for j in range(127, -1, -1):
        noise[i][j] = prenoise[i][(127-j)*2 + 1]

res = (img + noise)

for i in range(256):            #Не даю вылезти за границы дозволеного
    for j in range(256):
        if res[i][j] > 255:
            res[i][j] = 255
        if res[i][j] < 0:
            res[i][j] = 0

res = Image.fromarray(res.astype("uint8"), "L")
res.save("/home/kosta/Фото/Горизонтальные/256 256/Lenna/LennaCorrNoise.jpg")