import array as arr
from array import *

val = arr.array('i',[1,2,3,4,5,6,7,8,9])

for i in range(0,len(val)):
    print(val[i],end =" ")

#enhanced for loop
print('\n')
for x in val:
   print(x, end=",")

print('\n')

# print(val.typecode)

# val.reverse()

# for i in range(0,len(val)):
#     print(val[i],end =" ")

val.insert(1,50)    
val.append(100)
val[2] = 200 ## element replaced not shifted.

copyArray = array(val.typecode, (x for x in val))


for i in range(0,len(val)):
    print(val[i],end=' ')
