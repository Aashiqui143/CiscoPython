
with open("file1.txt",'rt') as inp:

    x=inp.read().replace("\n"," ")
    print(x)
'''for line in x:
    line=line.replace("\n","")
    print(line, end=" ")'''