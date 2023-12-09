class Image:
    def __init__(self, title_value = 'My image', res_value = '1920*1080', ext_value = 'png'):
        self.resolution = res_value
        self.title = title_value
        self.extension = ext_value
    def resize(self, new_res):
        self.resolution = new_res

i1 = Image('My car', '8000*6000', 'jpg')
i2 = Image('my home', '1280*720', 'jpg')
i1.resize('500*500')
i2.resize('650*650')

print(i1.title, i1.resolution, i1.extension)
print(i2.title, i2.resolution, i2.extension)