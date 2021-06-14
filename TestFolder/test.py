f = open('test.txt', 'r')
#for line in f.readlines():
#    print(line)


#for line in f:
#    print(line)

for idx, line in enumerate(f):
    print(idx, f.readline())
