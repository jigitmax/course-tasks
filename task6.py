def update_car_info(**car):
    car['is_available'] = True
    return car

my_car = update_car_info(brand = 'Toyota', biulding = 1995, color = 'red', price = 24999)
print(my_car)