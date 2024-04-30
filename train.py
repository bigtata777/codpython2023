print("hello world")
import numpy as np
import random

numeros =[random.random() for _ in range(100)]
funcion1 = lambda x:  (np.sqrt(x) + x**2) + (125*x**2 + 2*x  + 0.9*x + 5)/(np.cos(x*3)+100*x + x**5)
funcion2 = lambda x: (x**2- 0.8*x - 1)/(120*x**2)
output1 = []
output2 = []

for i in numeros:
    output1.append(funcion1(i))
    output2.append(funcion2(i))
print(output1)
print(output2)