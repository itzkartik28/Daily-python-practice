import numpy as np

arr=np.array([10,20,30,40,50,60,70])

print("orinal array")
print("array",arr)

#slicing
print("element from 1 to 4")
print(arr[1:5])

print("first 4 elements")
print(arr[:4])

print("elements from index 3 to end")
print(arr[3:])

print("alternative element")
print(arr[::2])

print("reverse elements")
print(arr[::-1])