theboard={'tl':' ', 'tm':' ', 'tr':' ',
          'ml':' ', 'mm':' ', 'mr':' ',
          'll':' ', 'lm':' ', 'lr':' '}

def printboard(board):
    print(board['tl'],'|',board['tm'],'|',board['tr'])
    print('- + - + -')
    print(board['ml'],'|',board['mm'],'|',board['mr'])
    print('- + - + -')
    print(board['ll'],'|',board['lm'],'|',board['lr'])
printboard(theboard)
turn=input("Enter who's turn is first 'x' or 'o':")
for i in range(9):
    print("enter the place",turn,'is palced')
    move=input("enter a white space:")
    if move in theboard.keys():
        theboard[move]=turn
        printboard(theboard)
        if turn=='x':
            turn='o'
        else:
            turn='x'
