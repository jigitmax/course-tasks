my_img = ('1920', '1080', 7765)

if len(my_img) == 2:
    info = f"{my_img[0]}x{my_img[1]}"
else:
    info = "Incorrect image formatting"

print(info)

lenstr = "String is long" if len(info)>15 else "String is short"

print(lenstr)