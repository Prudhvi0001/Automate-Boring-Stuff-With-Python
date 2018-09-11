inventory = {'arrow': 12, 'goldcoin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
addeditems = ['arrow', 'goldcoin', 'rope', 'goldcoin', 'dagger', 'goldcoin']


def addtoinventory(iventory, addeditems):
    for items in addeditems:
        inventory[items] += 1


def displayinventory(items):
    print("Inventory:")
    count = 0
    for keys in items.keys():
        print(inventory[keys], keys)
        count += inventory[keys]
    print("Total number of items: ", str(count))


addtoinventory(inventory, addeditems)
displayinventory(inventory)
