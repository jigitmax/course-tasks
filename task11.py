def dict_to_list(dict1: dict):
    list1 = []
    for k, v in dict1.items():
        if isinstance(k, int):
            t = (int(k)*2, v)
        else:
            t = (k, v)
        list1.append(t)
    return list1

test_dict = {321 : 1, 'dhfs': 3, 433.6: 5}

print(dict_to_list(test_dict))