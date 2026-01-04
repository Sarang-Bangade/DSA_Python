
from array import *

arr = array('i',[])
n = int(input("How many elements you want to insert"))

for i in range(0,n):
    arr.append(int(input('Enter next input')))

for x in arr:
    print(x, end=" ")