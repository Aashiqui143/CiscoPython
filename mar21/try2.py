import numpy as np
import array

x=np.ones((3,5), dtype=float)
print("\n",x)

#creating a matrix with a predefined value
x=np.full((3,5),1.23)
print("\n",x)

#create an array of even space between the given range of values
x=np.linspace(0, 1, 5)
print("\n",x)

#create a 3x3 array with mean 0 and standard deviation 1 in a given dimension
x=np.random.normal(0, 1, (3,3))
print("\n",x)

#create an identity matrix
x=np.eye(3)
print("\n",x)

#set a random seed
x=np.random.seed(9)
print("\n",x)

# Something
x1 = np.random.randint(10, size=6).reshape(2,3) #one dimension
x2 = np.arange(10).reshape(2,5) #two dimension
x3 = np.random.randint(10, size=(3,4,5)) #three dimension
print("\n",x1)
print("\n",x2)

print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print(x3)

arr=array.array('i')
for i in range(20):
    arr.append(i+1)
print(arr)


