import array
from array import *

val = array('i',[1,2,3,4,5,6])

for i in range(0,len(val)):
    print(val[i], end = " ")

print('\n')    

copyArray = array(val.typecode, (x*2 for x in val))    

for i in range(0,len(val)):
    print(copyArray[i], end = " ")