def wijzig(letterlijst):
    while len(letterlijst) > 0:
        letterlijst.pop()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)