dict1 = {'hfvgdg': 1, 'vhdefs': 2, 'vhhtqefs': 3}
dict2 = {k.upper(): v for k, v in dict1.items()}
print(dict2)

list1 = ['dfhgd', 'fd', 'efg', 'r', 'hfgt3r2','hdvgghsw', 'yegfyw263r']
list2 = [elem for elem in list1 if len(elem)>3]
print(list2)