my_fisrt_list = [1212, 'hfvgdjv', True, 3.76746]
my_second_list = [45572, False, 'ghg3dds']
res = my_fisrt_list + my_second_list
print(res)

my_fisrt_list.__iadd__(my_second_list)
print(my_fisrt_list)