import numpy as np
import scipy
import scipy.integrate

def trapezoid_rule(f, a, b):
    return (b - a) * 1/2 *(f(a) + f(b))
def simpsonovo_pravidlo(fce, a, b) :
    return ((b - a) / 6) * (fce(a) + 4 * fce((a + b) / 2) + fce(b))

# Funkce a jejich analytické integrály
def fce_poly(x):
    return x**3

def fce_harmonicka(x):
    return np.sin(x)

def fce_exp(x):
    return np.exp(x)

def integral_poly(a, b):
    return (b**4 - a**4) / 4

def integral_harmonic(a, b):
    return -np.cos(b) + np.cos(a)

def integral_exp(a, b):
    return np.exp(b) - np.exp(a)


a = 0
b = 10

#analitické reseni

integral_poly_analiticka = integral_poly(a, b)
integral_harmonic_analiticka = integral_harmonic(a, b)
integral_exp_analiticka = integral_exp(a, b)

#simpsonovo pravidlo

integral_poly_simpson = simpsonovo_pravidlo(fce_poly, a, b)
integral_harmonic_simpson = simpsonovo_pravidlo(fce_harmonicka, a, b)
integral_exp_simpson = simpsonovo_pravidlo(fce_exp, a, b)

#trapezoid

integral_poly_trapezoid = trapezoid_rule(fce_poly, a, b)
integral_harmonic_trapezoid = trapezoid_rule(fce_harmonicka, a, b)
integral_exp_trapezoid = trapezoid_rule(fce_exp, a, b)

print("Analitické reseni")
print("Polynom: ", integral_poly_analiticka)
print("Harmonicka funkce: ", integral_harmonic_analiticka)
print("Exponencialni funkce: ", integral_exp_analiticka, end="\n\n")

print("Simpsonovo pravidlo")
print("Polynom: ", integral_poly_simpson)
print("Harmonicka funkce: ", integral_harmonic_simpson)
print("Exponencialni funkce: ", integral_exp_simpson, end="\n\n")

print("Trapezoid")
print("Polynom: ", integral_poly_trapezoid)
print("Harmonicka funkce: ", integral_harmonic_trapezoid)
print("Exponencialni funkce: ", integral_exp_trapezoid)
