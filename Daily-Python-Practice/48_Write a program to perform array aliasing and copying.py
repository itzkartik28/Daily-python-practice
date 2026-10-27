import numpy as np

#creation of array
a=np.array([10,20,30])

#asling
b=a
b[0]=100

#after asling
print("array a",a)
print("array b",b)

#copying
c=a.copy()
c[1]=200

#after copying
print("array a",a)
print("array b",b)