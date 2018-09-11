inputfile = open('paris.jpg', 'rb')
outputfile = open('index.jpg', 'wb')
msg = inputfile.read(10)
while len(msg):
    outputfile.write(msg)
    msg = inputfile.read(10)
inputfile.close()
outputfile.close()
