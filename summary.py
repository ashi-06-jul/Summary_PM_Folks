print ("Hello World")
file = open ("w.txt",'r')
f = file.readlines()
for i in f:
    if '#' in i:
        print(i)
