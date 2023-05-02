list1=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
size=len(list1)
i=0
while i<size:
    
    if list1[i]>50:
        del list1[i]
        size-=1
    else:    
        i+=1
        
        

print(list1)