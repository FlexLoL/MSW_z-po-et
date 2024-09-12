import time
import numpy as np
import sympy as sp
import scipy.integrate as integrate

#skalární součin 
print("Skalární součin")
def skalar_soucin_obyc(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def skalar_soucin_numpy(v1, v2):
    return np.dot(v1, v2)

#měření
v1 = [11, 15, 13]
v2 = [18, 10, 7]
start = time.perf_counter()
f_sp = skalar_soucin_obyc(v1, v2)
vysledek1 = time.perf_counter() - start

start = time.perf_counter()
f_ob = skalar_soucin_numpy(v1, v2)
vysledek2 = time.perf_counter() - start

print(f"obyčejný pyton :{vysledek1}, scipy :{vysledek2}", end="\n\n")

#faktorial
print("Faktorial")
def faktorial_obyc(n : int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def faktorial_scipy(n : int) -> int:
    return sp.factorial(n)

#měření
start = time.perf_counter()
f_ob = faktorial_obyc(50)
vysledek1 = time.perf_counter() - start

start = time.perf_counter()
f_sp = faktorial_scipy(50)
vysledek2 = time.perf_counter() - start

print(f"obyčejný pyton :{vysledek1}, scipy :{vysledek2}", end="\n\n")

#integrační funkce
print("Integrační funkce")
def integral_obyc(fce, a, b, steps=10000):
    step_size = (b - a) / steps
    result = 0
    for i in range(steps):
        result += fce(a + i * step_size) * step_size
    return result

def intergral_scipy(fce, a, b):
    return integrate.quad(fce, a, b)[0]

#měření
start = time.perf_counter()
f_sp = integral_obyc(lambda x: x ** 2, 0, 5)
vysledek1 = time.perf_counter() - start

start = time.perf_counter()
f_ob = intergral_scipy(lambda x: x ** 2, 0, 5)
vysledek2 = time.perf_counter() - start

print(f"obyčejný pyton :{vysledek1}, scipy :{vysledek2}", end="\n\n")

#lineární rovnice
print("Lineární rovnice")
def linar_obyc(a, b):
    return -b / a if a != 0 else None

def linear_numpy(a, b):
    return np.linalg.solve([[a]], [b])

#měření
start = time.perf_counter()
f_sp = linar_obyc(-10, 21)
vysledek1 = time.perf_counter() - start

start = time.perf_counter()
f_ob = linear_numpy(-10, 21)
vysledek2 = time.perf_counter() - start

print(f"obyčejný pyton :{vysledek1}, scipy :{vysledek2}", end="\n\n")


#kvadratická rovnice
print("Kvadratická rovnice")
def kvadraticka_obyc(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        return -b / (2 * a),
    else:
        return None
    
def kvadraticka_sympy(a, b, c):
    x = sp.Symbol('x')
    solutions = sp.solve(a * x ** 2 + b * x + c, x)
    return solutions

#měření
start = time.perf_counter()
f_sp = kvadraticka_obyc(2, 12, 9)
vysledek1 = time.perf_counter() - start

start = time.perf_counter()
f_ob = kvadraticka_sympy(2, 12, 9)
vysledek2 = time.perf_counter() - start

print(f"obyčejný pyton :{vysledek1}, scipy :{vysledek2}", end="\n\n")


