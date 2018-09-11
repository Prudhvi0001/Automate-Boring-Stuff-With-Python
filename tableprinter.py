tabledata = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
widths=[]
for i in range(len(tabledata)):
    for j in range(len(tabledata[0])):
        widths=widths+[len(tabledata[i][j])]
maxwidth=max(widths)
def printtable(tabledata):
    for i in range(len(tabledata)):
        for j in range(len(tabledata[0])):
            print(tabledata[i][j].rjust(maxwidth+1),end='')
        print()
printtable(tabledata)
