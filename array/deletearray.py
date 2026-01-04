
from array import *

val = array('i', [1,2,3,4,5,6])
for i in range(0, len(val)):
    print(val[i], end =" ")

print('\n')

copyArray = array(val.typecode, (x for x in val))

copyArray.pop() # to delete the element from the array

copyArray.remove(5) # to directly delete the element


for i in range(0,len(copyArray)):
    print(copyArray[i],end =" ")    