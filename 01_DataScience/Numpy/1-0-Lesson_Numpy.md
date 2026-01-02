# 1. Matrix

- **Zero Matix</b> :** `numpy.zeros(shape, dtype=float, order='C', *, like=None)`
- **Ones Matrix :** `numpy.ones(shape, dtype=float, order='C', *, like=None)`
- **Constant Matrix :** `numpy.full(shape, fill_value, dtype=None, order='C', *, like=None)`
- **Empty :** (Random value) :  `numpy.empty(shape, dtype=float, order='C', *, like=None)`
- **Identity** **Matrix :** `numpy.identity(n, dtype=None)`
- **Linspace :** (config range) : `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`
- **Arange :** (config range) : `numpy.arange([start,] stop[, step,], dtype=None)`


``` python
# Zero Matrix
import numpy as np
a = np.zeros(5, dtype=int)
b = np.zeros((2,3))

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [0 0 0 0 0]
# =============================================
# [[0. 0. 0.]
#  [0. 0. 0.]]
 ```

</details>


``` python
# Ones Matrix
import numpy as np
a = np.ones(5, dtype=int)
b = np.ones((2,3))

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [1 1 1 1 1]
# =============================================
# [[1. 1. 1.]
#  [1. 1. 1.]]
 ```

</details>


``` python
# Constant Matrix
import numpy as np
a = np.full(5, 10)
b = np.full((2,3), 7)

print(a)    # imput number:5, value:10
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [10 10 10 10 10]
# =============================================
# [[7 7 7]
#  [7 7 7]]
 ```

</details>


``` python
# Empty
import numpy as np
a = np.empty(5)
b = np.empty((2,3))

print(a) # random 5 values [0-1] in list
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [5.e-324 5.e-324 5.e-324 5.e-324 5.e-324]
# =============================================
# [[1. 1. 1.]
#  [1. 1. 1.]]
 ```

</details>


``` python
# Identity Matrix
import numpy as np
a = np.identity(5)
b = np.identity(3)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
# =============================================
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
 ```

</details>


``` python
# Linspace (config range)
import numpy as np
a = np.linspace(1, 3, 10, dtype = int) #np.linspace(start, stop, number)
b = np.linspace(0, 1, 5)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [1 1 1 1 1 2 2 2 2 3]
# =============================================
# [0.   0.25 0.5  0.75 1.  ]
 ```

</details>


``` python
# Arange (config range)
import numpy as np
a = np.arange(1, 9, 2)      # np.arage(start, stop, step)
b = np.arange(0, 1, 0.2)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [1 3 5 7]
# =============================================
# [0.  0.2 0.4 0.6 0.8]
 ```

</details>


# 2. Random

- **rand :** `numpy.random.rand(d0, d1, ..., dn)`   # d0,...dn are dimension of matrix
- **randn :** `np.random.randn(d0, d1, ..., dn)`    # Standard normal distribution (mean 0, std 1)
- **randint :** `np.random.randint(low, high=None, size=None, dtype=int)` # [low,hitght)
- **shuffle :** `np.random.shuffle(x)`              # shuffle order in arr (list)


``` python
# rand  -> Random value [0, 1)
import numpy as np

a = np.random.rand()        # not indicate = value (0 dim)
b = np.random.rand(2)        # 1 dim
c = np.random.rand(2,3)     # 2 dim

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# 0.6697208511638658
# =============================================
# [0.57925947 0.08354378]
# =============================================
# [[0.59889974 0.2977149  0.61128553]
#  [0.34440612 0.69365838 0.87989882]]
```
</details>


``` python
# randn
import numpy as np

a = np.random.randn()        # not indicate = value (0 dim)
b = np.random.randn(2)        # 1 dim
c = np.random.randn(2,3)     # 2 dim

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# 1.2612488680530454
# =============================================
# [1.53260329 0.37524792]
# =============================================
# [[-0.10007651 -0.31421211 -1.09793232]
#  [ 0.17918088  0.26968506 -0.05270229]]
```
</details>


``` python
# randint
import numpy as np

a = np.random.randint(1, 11, 5)         # low, hight, size -> [low, hight)
b = np.random.randint(2)
c = np.random.randint(2,3)

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [10  9  3  2  4]
# =============================================
# 1
# =============================================
# 2
```
</details>


``` python
# choice
import numpy as np

a = np.random.choice([1,2,3,4], 2)  # random values in list, size
print(a)
```
<details>
<summary> Output </summary>

``` python
# [3 1]
```
</details>


``` python
# shuffle
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
```
<details>
<summary> Output </summary>

``` python
# [2 3 5 1 4]
```
</details>


# 3. Slice (Query data)

- **1 dimension :** a[2:], a[:4]
- **2 dimensions :** a[1:3, 1:]

``` python
# one dimension
import numpy as np

a = np.array([1,11,7,6,9])

print(a[2:])    # From index=2 to the last character  (start with index=0)
print("=============================================")
print(a[:4])    # From the first character to index=3 (4-1) -> a[:m] -> size=m (index=0 to m-1)
```
<details>
<summary> Output </summary>

``` python
# [7 6 9]
# =============================================
# [ 1 11  7  6]
```
</details>


``` python
# two dimensions
import numpy as np

a = np.array([[1,2,3,4], 
              [5,6,7,8], 
              [9,10,11,12]])

print(a[1:3, 1:])       # select row index = 1 to 2 (3-1), col index = 1 to last.
```
<details>
<summary> Output </summary>

``` python
[[ 6  7  8]
 [10 11 12]]
```
</details>


# 4. Mathematics Operations

``` python
## plus minus multiply divide power mod by digit
import numpy as np

a = np.arange(1,5) # [1,5)

print(f"a : {a}")
print("=============================================")
print(f"a+2 : {a+2}")      # Plus all elements (in array) by 2.
print("=============================================")
print(f"a-2 : {a-2}")      # Minus all elements (in array) by 2.
print("=============================================")
print(f"ax2 : {a*2}")      # Multiply all elements (in array) by 2.      
print("=============================================")
print(f"a/2 : {a/2}")      # Devide all elements (in array) by 2.
print("=============================================")
print(f"a^2 : {a**2}")     # Power all elements (in array) by 2.
print("=============================================")
print(f"a mod(2) : {a%2}")      # Mod all elements (in array) by 2.
```
<details>
<summary> Output </summary>

``` python
# a : [1 2 3 4]
# =============================================
# a+2 : [3 4 5 6]
# =============================================
# a-2 : [-1  0  1  2]
# =============================================
# ax2 : [2 4 6 8]
# =============================================
# a/2 : [0.5 1.  1.5 2. ]
# =============================================
# a^2 : [ 1  4  9 16]
# =============================================
# a mod(2) : [1 0 1 0]
```
</details>


``` python
# plus minus multiply divide power mod by arange [1 dimension]
import numpy as np

a = np.arange(1,5)          # [1,5)
b = np.array([2,4,6,8])     # 4 sizes

print(f"a : {a}")
print("=============================================")
print(f"b : {b}")
print("=============================================")
print(f"a+b : {a+b}")      # Plus array have to the same shapes
print("=============================================")
print(f"a-b : {a-b}")      # Minus array have to the same shapes
print("=============================================")
print(f"axb : {a*b}")      # Multiply array have to the same shapes (multiply scalar)      
print("=============================================")
print(f"a/b : {a/b}")      # Devide array have to the same shapes (devide scalar)   -> Don't !!! devidend is equal to 0
print("=============================================")
print(f"a^b : {a**b}")     # Power array have to the same shapes (power scalar)
print("=============================================")
print(f"a mod(b) : {a%b}") # Mod array have to the same shapes (mod scalar)
```
<details>
<summary> Output </summary>

``` python
# a : [1 2 3 4]
# =============================================
# b : [2 4 6 8]
# =============================================
# a+b : [ 3  6  9 12]
# =============================================
# a-b : [-1 -2 -3 -4]
# =============================================
# axb : [ 2  8 18 32]
# =============================================
# a/b : [0.5 0.5 0.5 0.5]
# =============================================
# a^b : [    1    16   729 65536]
# =============================================
# a mod(b) : [1 2 3 4]
```
</details>


# 5. Broadcasting


Solve the problem of calculating arrays with different dimensions. <br>

Boadcast Array that smaller was duplicated. <br>
Ex. array x 2 dim, array y 2 dim. -> array y 1 dim was boardcasted to array 2 dim to align with array x, compare dimensions from right to left.

<img src="image.png" alt="alt text" width="500" height="190">!

``` python
import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([1,2])
# a+b -> ValueError: operands could not be broadcast together with shapes (6,) (2,) 
x = np.array([[1,2], [3,4], [5,6]])
y = np.array([1,2,3])
# x+y -> ValueError: operands could not be broadcast together with shapes (3,2) (3,) 
x1 = np.array([[1,2], [3,4], [5,6]])
y1 = np.array([1,2]) # -> มันจะทำงานซ้ำ เป็น np.array([[1,2], [1,2], [1,2]])
print(x1+y1)
```
<details>
<summary> Output </summary>

``` python
# [[2 4]
#  [4 6]
#  [6 8]]
```
</details>


# 6. Function for Statistic

- **Function about statistic** # 1 or 2 dimension(s)

``` python
# Function about statistic 1 dimension
# sum, prod, mean, max, min, position of max/min
import numpy as np

a = np.array([10,5,4,6,99,100,50,30])

print(f"a: {a}")
print("=============================================")
print(f"sum: {a.sum()}")
print("=============================================")
print(f"product: {a.prod()}")
print("=============================================")
print(f"mean: {a.mean()}")
print("=============================================")
print(f"max: {a.max()}")
print("=============================================")
print(f"min: {a.min()}")
print("=============================================")
print(f"position (index) of max: {a.argmax()}")
print("=============================================")
print(f"position (index) of min: {a.argmin()}")
```
<details>
<summary> Output </summary>

``` python
# a: [ 10   5   4   6  99 100  50  30]
# =============================================
# sum: 304
# =============================================
# product: 17820000000
# =============================================
# mean: 38.0
# =============================================
# max: 100
# =============================================
# min: 4
# =============================================
# position (index) of max: 5
# =============================================
# position (index) of min: 2
```
</details>


``` python
## Function about statistic 2 dimensions
# sum, prod, mean, max, min, position of max/min
# axis 0 (Vertical), axis 1 (Horizontal)
import numpy as np

a = np.array([[10,20,30], [40,50,90], [80,100,5]])

print(f"a: {a}")
print("=============================================")
print(f"sum (align vertical (แนวตั้ง)): {np.sum(a, axis=0)}")
print("=============================================")
print(f"product (align vertical (แนวตั้ง)): {np.prod(a, axis=0)}")
print("=============================================")
print(f"mean (align horizontal (แนวนอน)): {np.mean(a, axis=1)}")
print("=============================================")
print(f"max (align horizontal (แนวนอน)): {np.max(a, axis=1)}")
print("=============================================")
print(f"min (align horizontal (แนวนอน)): {np.min(a, axis=1)}")
print("=============================================")
print(f"position (index) of max (align horizontal (แนวนอน)): {np.argmax(a, axis=1)}")
print("=============================================")
print(f"position (index) of min (align horizontal (แนวนอน)): {np.argmin(a, axis=1)}")
```
<details>
<summary> Output </summary>

``` python
# a: [[ 10  20  30]
#  [ 40  50  90]
#  [ 80 100   5]]
# =============================================
# sum (align vertical (แนวตั้ง)): [130 170 125]
# =============================================
# product (align vertical (แนวตั้ง)): [ 32000 100000  13500]
# =============================================
# mean (align horizontal (แนวนอน)): [20.         60.         61.66666667]
# =============================================
# max (align horizontal (แนวนอน)): [ 30  90 100]
# =============================================
# min (align horizontal (แนวนอน)): [10 40  5]
# =============================================
# position (index) of max (align horizontal (แนวนอน)): [2 2 1]
# =============================================
# position (index) of min (align horizontal (แนวนอน)): [0 0 2]
```
</details>


# 7. Dot product

- **Dot product :** a.dot(b) where a and b are arrays #multiple matrix

``` python
# Dot product
import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([[11,12], [13,14]])
c = a.dot(b)

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [[1 2]
#  [3 4]]
# =============================================
# [[11 12]
#  [13 14]]
# =============================================
# [[37 40]
#  [85 92]]
```
</details>


# 8. Insert / Delete

- **Insert 1 dim:** `np.insert(a, index, value)`     where "a" is a array
- **Insert >=2 dims:** `np.insert(a, index, value, axis=...)`     where "a" is a array
- **Delete :** `np.delete(a, index)`            where "a" is a array
- **Delete >=2 dims:** `np.delete(a, index, axis=...)`            where "a" is a array

``` python
# insert 1 dim : can indicate position of elements
import numpy as np

a = np.array([1,2,4,5,8])
b = np.append(a, 100)
c = np.insert(a, 1, 100)    # insert index = 1 with value = 100
d = np.insert(a, (1,3), (100,200))
print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
print("=============================================")
print(d)
```
<details>
<summary> Output </summary>

``` python
[1 2 4 5 8]
=============================================
[  1   2   4   5   8 100]
=============================================
[  1 100   2   4   5   8]
=============================================
[  1 100   2   4 200   5   8]
```
</details>


``` python
# insert 2 dims : can indicate position of elements
import numpy as np

a = np.array([[1,2], [10,11]])
b = np.insert(a, 1, 100, axis=0)
c = np.insert(a, 1, [800,900], axis=1)
print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [[ 1  2]
#  [10 11]]
# =============================================
# [[  1   2]
#  [100 100]
#  [ 10  11]]
# =============================================
# [[  1 800   2]
#  [ 10 900  11]]
```
</details>


``` python
# delete 1 dim
import numpy as np

a = np.arange(1,11)
b = np.delete(a, 2)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [ 1  2  3  4  5  6  7  8  9 10]
# =============================================
# [ 1  2  4  5  6  7  8  9 10]
```
</details>


``` python
# delete 2 dim
import numpy as np

a = np.arange(1,13).reshape(4,3)
b = np.delete(a, 2, axis=0)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# =============================================
# [[ 1  2  3]
#  [ 4  5  6]
#  [10 11 12]]
```
</details>


# 9. Split

- **Split 1 dim :** `np.split(a, split_value)`     where "a" is a array / *split have to divisible*.
- **Split >=2 dims :** `np.[v/h]split(a, split_value)`     where "a" is a array / *split have to divisible*.


``` python
# Split 1 dim
import numpy as np

a = np.arange(1,21)
b = np.split(a,4)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
# =============================================
# [array([1, 2, 3, 4, 5]), array([ 6,  7,  8,  9, 10]), array([11, 12, 13, 14, 15]), array([16, 17, 18, 19, 20])]
```
</details>


``` python
# Split >=2 dims
import numpy as np

a = np.arange(1,21).reshape(5,4)
b = np.hsplit(a, 4)
c = np.vsplit(a, 5)

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]s
# =============================================
# [array([[ 1],
#        [ 5],
#        [ 9],
#        [13],
#        [17]]), array([[ 2],
#        [ 6],
#        [10],
#        [14],
#        [18]]), array([[ 3],
#        [ 7],
#        [11],
#        [15],
#        [19]]), array([[ 4],
#        [ 8],
#        [12],
#        [16],
#        [20]])]
# =============================================
# [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]]), array([[13, 14, 15, 16]]), array([[17, 18, 19, 20]])]
```
</details>

