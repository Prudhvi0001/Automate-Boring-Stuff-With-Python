def commacode(spam):
    print("'", end='')

    for i in range(len(spam) - 1):
        print(spam[i], end=',')
    print('end', spam[-1], "'")

commacode(['hello', 'rahul', 'supriya', 'parvathi'])
