print("hello world")
import numpy as np
import random
## cambios en cabecera
numeros =[random.random() for _ in range(1000)]
funcion1 = lambda x:  (np.sqrt(x) + x**2) + (125*x**2 + 2*x  + 0.9*x + 5)/(np.cos(x*3)+100*x + x**5)
funcion2 = lambda x: 120*np.sqrt((x**4- 0.8*x**3 - x)/(120*x**2))
funcion3 = lambda x: 100*np.cos(x**2) + x**2 -x
output1 = []
output2 = []
output3 = []

for i in numeros:
    output1.append(funcion1(i))
    output2.append(funcion2(i))
    output3.append(funcion3(i))
print(output1)
print(output2)
print(output3)

import numpy as np
def funcion(x):
    
    y = 1/(1- np.exp(-x))
    
    return y
probas  = [funcion(i)  for i in np.linspace(-1,2)]
print(probas)
