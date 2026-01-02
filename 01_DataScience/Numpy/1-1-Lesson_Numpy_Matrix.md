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

