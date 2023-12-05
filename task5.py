def merge_list_to_dict(first_list, second_lst):
    a = first_list
    b = second_lst
    c = zip(a, b)
    d = dict(c)
    return d

a1 = [2132, 4534, 74, 22455]
b1 = ['gfghdsh', 'hgvyuertf763', 'fdvgdhgf76trfd', 'hyvg762trfshvwy']

m = merge_list_to_dict(first_list=a1, second_lst=b1)
print(m)

a2 = [4243, 334, 7653, 645632, 65345]
b2 = ['vhvg', 'hgsfdh', 'vhdvh36tw', 'vdghvf63', 'tet76tfd']
m1 = merge_list_to_dict(a2, second_lst=b2)
print(m1)