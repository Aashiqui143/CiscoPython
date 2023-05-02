z=int(input("Enter a range number = "))
list0=list(int(input("Enter list element["+str(i)+"] = ")) for i in range(z))
print(list0)

list1=[]
list2=[]
list3=[]
count=0
for i in list0:
    if count<3:
        count+=1
        list1.append(i)
    elif count>=3 and count<6:
        count+=1
        list2.append(i)
    elif count>=6:
        count+=1
        list3.append(i)
print(list1)
print(list2)
print(list3)

'''sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size'''
