def say():
    name = input('your name : ')
    admin = 'jack'
    if name == admin:
        print('hello admin!')
    else:
        print('hello '+ name)
    a = 0
    while a < 10:
        print(a)
        a += 1

    input('press enter to exit : ')

say()
