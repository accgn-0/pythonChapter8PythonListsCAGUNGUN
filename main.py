fhand = open('romeo.txt')
for line in fhand:
    #line = line.rstrip()
    #words = line.strip()
    line = line.rsplit()
    #print(words[0:5])
    line.sort()
    print(line)
