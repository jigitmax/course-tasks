def filter_list(fl, t):
    result = []
    for i in fl:
        if isinstance(i, t) == False:
            result.append(i)
    return result


print(filter_list([35, True, 'abc', 10, 10.5], int))