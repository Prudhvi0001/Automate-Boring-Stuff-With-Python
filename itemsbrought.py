allguests = {'alice': {'apples': 5, 'oranges': 6},
             'bob': {'toys': 3, 'bread': 10},
             'diana': {'apples': 4, 'jam&butter': 2}}


def itemsbrought(guests, item):
    numbrought = 0
    for k, v in guests.items():
        numbrought = numbrought + v.get(item, 0)
    return numbrought


print(str(itemsbrought(allguests, 'apples')))
