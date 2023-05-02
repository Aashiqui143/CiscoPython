import time
import datetime
i=0
current=str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))

#current=current.replace(" ","_")
out=open("output_{current}.txt".format(current=current),'w')
#out.write("jfhgcvhjv") 
while i<20:
    out.write("{x}  True-----True-----True".format(x=i+1))
    print(i+1)
    time.sleep(1)
    out.write("\n")
    i+=1
out.close()
print("Done")
exit()