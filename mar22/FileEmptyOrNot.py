with open("file2.txt",'rt') as inp:
    x=inp.readlines()

if len(x)==0:
    print("Empty file")
else:
    print("Not an Empty file")