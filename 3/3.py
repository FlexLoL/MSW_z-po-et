import numpy as np
import time
import matplotlib.pyplot as plt

# Jacobiho iterační metoda
def jacobi(A, b, niteraci):
    x =np.ones(len(A))
    D = np.diag(A)
    L = np.tril(A, k = -1)
    U = np.triu(A, k = 1)
    for i in range(niteraci):
        x = (b - np.matmul((L + U),x))/D
    return x

def gaussian_elimination(A, b):
    n = len(A)   
    Ab = np.column_stack((A, b)).astype(np.float64)  
    for i in range(n):
        if Ab[i, i] == 0.0:
            print('Dělení nulou!')
        for j in range(i + 1, n):
            ratio = Ab[j, i] / Ab[i, i]
            Ab[j] -= ratio * Ab[i] 

    # Zpětná substituce
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, :-1], x)) / Ab[i, i]
    
    return x

# Měření času pro přímou a iterativní metodu
def measure_time(matrix_size):
    A = np.random.rand(matrix_size, matrix_size)  
    b = np.random.rand(matrix_size)  
    # Přímá metoda
    start_time = time.perf_counter()
    gaussian_elimination(A, b)
    direct_time = time.perf_counter() - start_time

    # Iterační metoda (Jacobi)
    start_time = time.perf_counter()
    jacobi(A, b, 20)  
    iterative_time = time.perf_counter() - start_time

    return direct_time, iterative_time

# Testování pro různé velikosti matic
matrix_sizes = range(1, 10, 1)
direct_times = []
iterative_times = []

for size in matrix_sizes:
    direct_time, iterative_time = measure_time(size)
    direct_times.append(direct_time)
    iterative_times.append(iterative_time)

# Vykreslení grafu
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, direct_times, label='Přímá metoda (LU rozklad)', marker='o')
plt.plot(matrix_sizes, iterative_times, label='Iterační metoda (Jacobi)', marker='x')
plt.xlabel('Velikost matice')
plt.ylabel('Průměrný čas (sekundy)')
plt.title('Porovnání přímé a iterační metody pro řešení soustavy lineárních rovnic')
plt.legend()
plt.grid(True)
plt.show()