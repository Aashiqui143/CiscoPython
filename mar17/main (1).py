beatles=[]
# step 1
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
list1=[]
for i in range(2):
    z=input("Enter a name = ")
    beatles.append(z)
    list1.append(z)
print("Step 3:", beatles)

# step 4
for i in list1:
    y=beatles.index(i)
    del beatles[y]
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

