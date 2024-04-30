print("hello world")
import numpy as np
import random

numeros =[random.random() for _ in range(100)]
funcion = lambda x:  (np.sqrt(x) + x**2) + (125*x**2 + 2*x  + 0.9*x + 5)/(np.cos(x*3)+100*x + x**5)
output = []

for i in numeros:
    output.append(funcion(i))
print(output)