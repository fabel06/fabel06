file = open('faruk.txt')


file.close()

#read the file and store all the lines in list
#reverse the list back to the file
with open('faruk.txt') as reader:
    content = reader.readlines()#[abc,bvs,cat,dog]
    reversed(content)
    with open('faruk.txt','w') as writer:
        for line in reversed(content):

            writer.write(line)
