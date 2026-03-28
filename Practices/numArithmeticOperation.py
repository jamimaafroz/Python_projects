import numpy as np

var = np.array([1,2,3,4])

varAdd = var+3
print(var)
print(varAdd)#added 3 with all the elements in the arrray

var1 = np.array([1,2,3,4])
var2 = np.array([4,3,2,1])
sumVar = var1+var2#basic arithmetic way to perform addition
sum2 = np.add(var1,var2)#numpy function for addition
print(sumVar)
print(sum2)

#2D Array 
array2d = np.array([[1,2,3,4],[5,6,7,8]])
array2d2 = np.array([[1,2,3,4],[5,6,7,8]])
sum2Darray = array2d+array2d2
Mul2Darray = array2d*array2d2
print(array2d)
print(sum2Darray)
print(Mul2Darray)