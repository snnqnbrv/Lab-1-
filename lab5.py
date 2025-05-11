import math

def g(x):
    return math.atan(2 * x) - 1

def simple_iteration(x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            print(f"Kök təqribi: {x1} (iterasiya sayı: {i + 1})")
            return x1
        x0 = x1
    print("İterasiya limiti aşdı!")
    return None

x0 = 0.5  
simple_iteration(x0)
