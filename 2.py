import os
from PIL import Image, ImageFilter

x = r"91"
y = r"92"

a = os.listdir(x)
filename = []

for file in a:
    p1 = os.path.join(y, file) # join объединение
    filename.append(file)

    for i in filename:
        if i.lower().endswith(('.jpg', '.png')):
            img = Image.open(os.path.join(x, i))
            img_f = img.filter(ImageFilter.EMBOSS)
            img_f.save(p1)