# Ex 1. Secret Path
import numpy as np
import math

num_eq = int(input("Input the number of equations: "))
coeffs = []
free_Terms = []

for i in range(num_eq):
    equation = input(f"Input the coefficients of equation {i+1} (space separated): ")
    coeffs.append(list(map(float, equation.split())))
    free_term = float(input(f"Input the free term of equation {i+1} (after sign =): "))
    free_Terms.append(free_term)

coeffs_matrix = np.array(coeffs)
free_Terms_vector = np.array(free_Terms)
solution = np.linalg.solve(coeffs_matrix, free_Terms_vector)
print("===========================================================================")
print("Roots:")
for i in range(len(solution)):
    print(f'x{i+1} = {solution[i]}')
