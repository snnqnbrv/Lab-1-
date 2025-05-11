import math

A = [
    [4, 2, 3],
    [1, 9, 5],
    [6, 7, 16]
]
n = len(A)  
cem = 0

for i in range(n):
    cem += math.sqrt(A[i][i])  

print("Baş diaqonalda yerləşən elementlərin kvadrat köklərinin cəmi:", cem)
