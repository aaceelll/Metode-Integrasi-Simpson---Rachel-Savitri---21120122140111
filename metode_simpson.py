# -*- coding: utf-8 -*-
"""Metode_Trapezoid.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/aaceelll/Metode-Integrasi-Trapezoid---Rachel-Savitri---21120122140111/blob/main/Metode_Trapezoid.ipynb

Rachel Savitri - 21120122140111 - Kelas C

Metode Simpson 1/3
"""

import numpy as np
import time
import math

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode Simpson 1/3
def simpson_integration(a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    integral *= h / 3
    return integral

# Menghitung galat RMS
def rms_error(estimated, actual):
    return np.sqrt((estimated - actual) ** 2)

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Loop untuk menghitung integral, galat RMS, dan waktu eksekusi untuk setiap N
results = []
for N in N_values:
    start_time = time.time()
    estimated_pi = simpson_integration(0, 1, N)
    end_time = time.time()
    rms = rms_error(estimated_pi, pi_ref)
    execution_time = end_time - start_time
    results.append((N, estimated_pi, rms, execution_time))

# Menampilkan hasil
for result in results:
    N, estimated_pi, rms, execution_time = result
    print(f'N = {N}:')
    print(f'  Estimated Pi = {estimated_pi}')
    print(f'  RMS Error = {rms}')
    print(f'  Execution Time = {execution_time} seconds')
    print()