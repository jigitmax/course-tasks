def image_info(info: dict):
    try:
        title = info['image_title']
        im_id = info['image_id']
    except KeyError as e:
        raise TypeError(e)
    print(f"Image '{title}' has id {im_id}" )

dict_one = {'image_title' : 'My_cat', 'image_id' : 5136}
dict_two = {'image_title' : 'My_cat'}
dict_three = {'image_id' : 5136}
dict_four = {'nomer' : 56675}
try:
    image_info(dict_one)
except Exception as e:
    print('Нет ключа '+str(e))
try:
    image_info(dict_two)
except Exception as e:
    print('Нет ключа '+str(e))
try:
    image_info(dict_three)
except Exception as e:
    print('Нет ключа '+str(e))

try:
    image_info(dict_four)
except Exception as e:
    print('Нет ключа '+str(e))