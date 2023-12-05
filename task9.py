def route_info(info: dict):
    if info.get('distance'):
        ret_str = f"Distance to your destination is {info['distance']}"
    elif info.get('speed') and info.get('time'):
        ret_str = f"Distance to your destination is {info['speed']*info['time']}"
    else:
        ret_str = "No distance info is available"
    return ret_str

dict_one = {'distance' : 256}
print(route_info(dict_one))

dict_two = {'speed' : 100, 'time': 5}
print(route_info(dict_two))

dict_three = {}
print(route_info(dict_three))