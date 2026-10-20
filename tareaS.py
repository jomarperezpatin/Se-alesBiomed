import numpy as np
import matplotlib.pyplot as plt

# vector de tiempo
n= np.array([-2, -1, 0, 1, 2])

# 1. Impulso unitario

def delta(n): 
    return np.where(n == 0, 1, 0)

# 2. Escalón unitario

def step(n):
    return np.where(n >= 0, 1, 0)

# 3. Rampa unitaria
def ramp(n):
    return np.where(n >= 0, n + 1, 0)

# 4. Funcion rectangular

def rect_N(n, N):
    return np.where(np.abs(n) <= N/2, 1, 0)

# 5. Función triangular

def tri_N(n, N):
    return np.maximum( 1 - np.abs(n)/N , 0)

# 6. Funcion coseno

def coseno(n, F, Fs):
    return np.cos(2 * np.pi * (F/Fs) * n)

# 7. Función seno
def seno(n, F, Fc):
    return np.sin(2 * np.pi * (F/Fc) * n)

#Valores de señales

print("n =", n)
print("delta(n) =", delta(n))
print("u(n) =", step(n))
print("r(n) =", ramp(n))

# Parametros
N = 2
F = 1
Fs = 5
Fc = 5 

print("rect_N(n, N) =", rect_N(n, N))
print("tri_N(n, N) =", tri_N(n, N))
print("coseno(n, F, Fs) =", np.round(coseno(n, F, Fs), 2))
print("seno(n, F, Fc) =", np.round(seno(n, F, Fc), 2))

# Graficas
plt.figure(figsize=(10, 10))

plt.subplot(4, 2, 1)
plt.stem(n, delta(n))
plt.title('Impulso unitario')
plt.grid()

plt.subplot(4, 2, 2)
plt.stem(n, step(n))
plt.title('Escalón unitario')
plt.grid()

plt.subplot(4, 2, 3)
plt.stem(n, ramp(n))
plt.title('Rampa unitaria')
plt.grid()

plt.subplot(4, 2, 4)
plt.stem(n, rect_N(n, N))
plt.title('Función rectangular')
plt.grid()

plt.subplot(4, 2, 5)
plt.stem(n, tri_N(n, N))
plt.title('Función triangular')
plt.grid()

plt.subplot(4, 2, 6)
plt.stem(n, coseno(n, F, Fs))
plt.title('Función coseno')
plt.grid()

plt.subplot(4, 2, 7)
plt.stem(n, seno(n, F, Fc))
plt.title('Función seno')
plt.grid()

plt.tight_layout()
plt.show()