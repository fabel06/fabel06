file = open('faruk.txt')
#Read all the contetents of file
#read n number of characters by passing parameter
#print(file.read())
#pread one single line at a time readline()
#print(file.readline())
#print(file.readline())



#print line by line using readline method

line = file.readline()
while line !="":
    print(line)
    line = file.readline()

#values = [abc, bvdsf, "cat",dog,elephant]
for line in file.readlines():
    print(line)



file.close()

