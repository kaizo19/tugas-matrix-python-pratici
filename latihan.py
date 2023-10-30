import numpy as np
#penjumlahan 
matrik_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrik_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

jumlah = np.add(matrik_1, matrik_2)
print(jumlah)
#pengurangan 

kurang = np.subtract(matrik_1, matrik_2)
print(kurang)

#perkalian matrik
matrik1 = np.array([[1, 2], [3, 4]])
matrik2 = np.array([[5, 6], [7, 8]])

perkalian = np.dot(matrik1, matrik2)
print(perkalian)

#transpose matrix
matrik = np.array([[1, 2], [3, 4], [5, 6]])

transpose = np.transpose(matrik)
print(transpose)

#invers matrik
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

invers = np.linalg.inv(matrix)
print(invers)

#identitas matrix

matrix_identitas = ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

ident = np.eye(matrix_identitas)
print(ident)

#reshape matrik
matrix_reshape = ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

reshape = np.reshape(matrix_reshape)
print(reshape)