while True:
    a = int(input('First number: '))
    b = int(input('Seecond number: '))
    try:
        c = a / b
        print(c)
    except ZeroDivisionError:
        print('Sorry ! You are dividing by zero')

    q = input('Continie? (yes or no): ')
    if q == 'yes':
        continue
    if q == 'no':
        break