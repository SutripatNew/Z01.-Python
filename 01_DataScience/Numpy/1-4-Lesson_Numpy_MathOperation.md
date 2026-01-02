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

