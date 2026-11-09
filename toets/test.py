def isDeelbaarDoor(x, y):
    if x > y:
        return print(f'{x} is inderdaad deelbaar door {y}')
    else:
        return print(f'helaas, {x} is niet deelbaar door {y}')


(isDeelbaarDoor(10, 2))