import numpy as np
import sympy as sp

#funkce sinus
def fce(x):
    return np.sin(x)

def derovace_analiticka(x):
    return np.cos(x)

def derivace_se_statickym_krokem(fce, x, krok):
    return (fce(x + krok) - fce(x - krok)) / (2 * krok)

def derivace_s_adaptabilnim_krokem(f, x, pocatecni_krok, tol):
    krok = pocatecni_krok
    while True:
        darivace_1 = (f(x + krok) - f(x - krok)) / (2 * krok)
        polovicni_krok = krok / 2
        darivace_2 = (f(x + polovicni_krok) - f(x - polovicni_krok)) / (2 * polovicni_krok)
        if np.abs(darivace_1 - darivace_2) < tol:
            return darivace_2
        krok /= 2


x = 1.0
krok = 0.1
tol = 1e-6

# Analytické řešení
derivative_analytical = derovace_analiticka(x)

# Numerická derivace se statickým krokem
derivative_static = derivace_se_statickym_krokem(fce, x, krok)

# Numerická derivace s adaptivním krokem
derivative_adaptive = derivace_s_adaptabilnim_krokem(fce, x, krok, tol)



print(f"Analytická derivace: {derivative_analytical}")
print(f"Numerická derivace se statickým krokem: {derivative_static}")
print(f"Numerická derivace s adaptivním krokem: {derivative_adaptive}")
