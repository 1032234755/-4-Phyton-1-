
import numpy as np

def gauss_jordan(a, b):
    n = len(b)
    for i in range(n):
        if a[i][i] == 0.0:
            raise ValueError("Деление на ноль!")
        
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]
                
                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    
    x = np.zeros(n)
    for i in range(n):
        x[i] = a[i][n]/a[i][i]
    
    return x

a = np.array([[1, -1, 1, -2, -20], 
              [9, -1, 1, 8, 60], 
              [-7, 8, 0, -6, -60], 
              [3, -5, 0, -6, -44]], float)

b = np.array([-20, 60, -60, -44], float)

solution = gauss_jordan(a, b)
print("Решение методом Гаусса:", solution)
