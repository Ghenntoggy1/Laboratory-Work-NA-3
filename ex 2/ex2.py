# Ex 2. Influence network
import numpy as np

with open('matrix.txt', 'r') as file:
    matrix = eval(file.read())  # citim matricea din txt

connectivity_matrix = np.array(matrix[1:])  # cream matricea fara primul rand

numeric_matrix = connectivity_matrix[:, 1:].astype(float)  # cream matricea fara prima coloana

eigenvalues, eigenvectors = np.linalg.eig(numeric_matrix)  # aflam eigenvalues si eigenvectors

dominant_index = np.argmax(eigenvalues)  # gasim indexul la cel mai influent eigenalue

dominant_eigenvalue = eigenvalues[dominant_index]  # luam cel mai influent eigenvalue
dominant_eigenvector = eigenvectors[:, dominant_index]  # luam eigenvectorii corespunzatori acestui eigenvalue influent

normalized_eigenvector = dominant_eigenvector / np.sum(dominant_eigenvector)  # normalizam vectorii corespunzatori

sorted_indices = np.argsort(normalized_eigenvector)[::-1]  # ordonam indicii eigenvectorilor influent lista in ordine descrescatoare

names = connectivity_matrix[:, 0]  # luam lista cu nume

print("Key Individuals:")
for index in sorted_indices:
    print(names[index], normalized_eigenvector[index])
