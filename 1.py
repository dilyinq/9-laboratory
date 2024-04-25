import os
from PIL import Image, ImageFilter

x = r"91"
y = r"92"

a = os.listdir(x) # функция для получения списка файлов из папки х
filename = [ ] # список для добавления фото

for file in a: # проходимся по фото и применяем путь к папке у
    p1 = os.path.join(y, file)
    filename.append(file) # добавляет имя файла в список filename.

    for i in filename:
        img = Image.open(os.path.join(x, i))
        img_f = img.filter(ImageFilter.EMBOSS)
        img_f.save(p1)

