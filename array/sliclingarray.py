from array import *

val = array('i',[1,2,3,4,5,6,7,8,9,10])

sliced_array1 = val[2 : 5] #from position 2 to 5 // :- 3 4 5

sliced_array2 = val[2 : -3] #starting from pos 2 and del last 3 elements // :- 3 4 5 6 7

sliced_array3 = val[:: -1] #reversing the element
for i in range(0, len(sliced_array3)):
    print(sliced_array3[i] , end =" ")