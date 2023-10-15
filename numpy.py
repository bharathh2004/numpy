
1.Create a null vector of size 10 but the fifth value which is 1
x=np.zeros(10)
x[4]=1

2. Create a vector with values ranging from 10 to 49.
import numpy as np
a = np.arange(10,49)
print(a)

3. Create a 3x3 matrix with values ranging from 0 to 8

import numpy as np
x =  np.arange(0, 18).reshape(3,3)
print(x)

4. Find indices of non-zero elements from [1,2,0,0,4,0]

A = [1,2,0,0,4,0]
find(A)

5. Create a 10x10 array with random values and find the minimum and maximum values
import numpy as np

x = np.random.randint((5,5))
print(x) 

xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)


6. Create a random vector of size 30 and find the mean value

import numpy as np
x = np.random.randint(30)
print(x)
x.sort()
print("Sorted array:")
print(x)