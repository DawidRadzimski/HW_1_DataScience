import numpy as np

# Zadanie 1: Utwórz jednowymiarową tablicę (wektor) z pierwszymi 10 dodatnimi liczbami całkowitymi i wyświetl jej wartość.
vector_10 = np.arange(1, 11)
print("Zadanie 1:", vector_10)

# Zadanie 2: Utwórz dwuwymiarową tablicę (macierz) o rozmiarze 3x3, wypełnij ją zerami i wyświetl jej wartość.
matrix_3x3_zeros = np.zeros((3, 3))
print("\nZadanie 2:\n", matrix_3x3_zeros)

# Zadanie 3: Utwórz tablicę o rozmiarze 5x5, wypełnij ją losowymi liczbami całkowitymi z zakresu od 1 do 10 i wyświetl jej wartość.
matrix_5x5_random = np.random.randint(1, 11, size=(5, 5))
print("\nZadanie 3:\n", matrix_5x5_random)

# Zadanie 4: Utwórz tablicę o rozmiarze 4x4, wypełnij ją losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i wyświetl jej wartość.
matrix_4x4_random_floats = np.random.rand(4, 4)
print("\nZadanie 4:\n", matrix_4x4_random_floats)

# Zadanie 5: Utwórz dwie jednowymiarowe tablice o rozmiarze 5, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i wykonaj na nich operacje dodawania, odejmowania i mnożenia.
vector_5_a = np.random.randint(1, 11, size=5)
vector_5_b = np.random.randint(1, 11, size=5)
print("\nZadanie 5:\nvector_5_a:", vector_5_a)
print("vector_5_b:", vector_5_b)
print("Addition:", vector_5_a + vector_5_b)
print("Subtraction:", vector_5_a - vector_5_b)
print("Multiplication:", vector_5_a * vector_5_b)

# Zadanie 6: Utwórz dwa wektory o rozmiarze 7, wypełnij je losowymi liczbami i znajdź ich iloczyn skalarny.
vector_7_a = np.random.random(7)
vector_7_b = np.random.random(7)
dot_product = np.dot(vector_7_a, vector_7_b)
print("\nZadanie 6:\nvector_7_a:", vector_7_a)
print("vector_7_b:", vector_7_b)
print("Dot product:", dot_product)

# Zadanie 7: Utwórz dwie macierze o rozmiarach 2x2 i 2x3, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i pomnóż je.
matrix_2x2 = np.random.randint(1, 11, size=(2, 2))
matrix_2x3 = np.random.randint(1, 11, size=(2, 3))
matrix_product = np.dot(matrix_2x2, matrix_2x3)
print("\nZadanie 7:\nmatrix_2x2:\n", matrix_2x2)
print("matrix_2x3:\n", matrix_2x3)
print("Product:\n", matrix_product)

# Zadanie 8: Utwórz macierz o rozmiarze 3x3, wypełnij ją losowymi liczbami całkowitymi z zakresu od 1 do 10 i znajdź jej odwrotność.
matrix_3x3 = np.random.randint(1, 11, size=(3, 3))
try:
    matrix_inverse = np.linalg.inv(matrix_3x3)
    print("\nZadanie 8:\nmatrix_3x3:\n", matrix_3x3)
    print("Inverse:\n", matrix_inverse)
except np.linalg.LinAlgError:
    print("\nZadanie 8: Macierz nie jest odwracalna.")

# Zadanie 9: Utwórz macierz 4x4, wypełnij ją losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i przetransponuj ją.
matrix_4x4 = np.random.rand(4, 4)
matrix_transpose = matrix_4x4.T
print("\nZadanie 9:\nmatrix_4x4:\n", matrix_4x4)
print("Transpose:\n", matrix_transpose)

# Zadanie 10: Utwórz macierz o rozmiarze 3x4 i wektor o rozmiarze 4, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i pomnóż macierz przez wektor.
matrix_3x4 = np.random.randint(1, 11, size=(3, 4))
vector_4 = np.random.randint(1, 11, size=4)
matrix_vector_product = np.dot(matrix_3x4, vector_4)
print("\nZadanie 10:\nmatrix_3x4:\n", matrix_3x4)
print("vector_4:", vector_4)
print("Product:", matrix_vector_product)

# Zadanie 11: Utwórz macierz o rozmiarze 2x3 i wektor o rozmiarze 3, wypełnij je losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i pomnóż macierz przez wektor.
matrix_2x3 = np.random.rand(2, 3)
vector_3 = np.random.rand(3)
matrix_vector_product_floats = np.dot(matrix_2x3, vector_3)
print("\nZadanie 11:\nmatrix_2x3:\n", matrix_2x3)
print("vector_3:", vector_3)
print("Product:", matrix_vector_product_floats)

# Zadanie 12: Utwórz dwie macierze o rozmiarze 2x2, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i wykonaj ich mnożenie pierwiastkowe.
matrix_2x2_a = np.random.randint(1, 11, size=(2, 2))
matrix_2x2_b = np.random.randint(1, 11, size=(2, 2))
elementwise_multiplication = matrix_2x2_a * matrix_2x2_b
print("\nZadanie 12:\nmatrix_2x2_a:\n", matrix_2x2_a)
print("matrix_2x2_b:\n", matrix_2x2_b)
print("Element-wise multiplication:\n", elementwise_multiplication)

# Zadanie 13: Utwórz dwie macierze o rozmiarze 2x2, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i znajdź ich iloczyn.
matrix_2x2_c = np.random.randint(1, 11, size=(2, 2))
matrix_2x2_d = np.random.randint(1, 11, size=(2, 2))
matrix_product_cd = np.dot(matrix_2x2_c, matrix_2x2_d)
print("\nZadanie 13:\nmatrix_2x2_c:\n", matrix_2x2_c)
print("matrix_2x2_d:\n", matrix_2x2_d)
print("Product:\n", matrix_product_cd)

# Zadanie 14: Utwórz macierz 5x5, wypełnij ją losowymi liczbami całkowitymi z zakresu od 1 do 100 i znajdź sumę elementów macierzy.
matrix_5x5_large = np.random.randint(1, 101, size=(5, 5))
matrix_sum = np.sum(matrix_5x5_large)
print("\nZadanie 14:\nmatrix_5x5_large:\n", matrix_5x5_large)
print("Sum of elements:", matrix_sum)

# Zadanie 15: Utwórz dwie macierze o rozmiarze 4x4, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i znajdź ich różnicę.
matrix_4x4_e = np.random.randint(1, 11, size=(4, 4))
matrix_4x4_f = np.random.randint(1, 11, size=(4, 4))
matrix_difference = matrix_4x4_e - matrix_4x4_f
print("\nZadanie 15:\nmatrix_4x4_e:\n", matrix_4x4_e)
print("matrix_4x4_f:\n", matrix_4x4_f)
print("Difference:\n", matrix_difference)

# Zadanie 16: Utwórz macierz 3x3, wypełnij ją losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i znajdź wektor kolumnowy zawierający sumę elementów każdego wiersza macierzy.
matrix_3x3_floats = np.random.rand(3, 3)
row_sums = np.sum(matrix_3x3_floats, axis=1)
print("\nZadanie 16:\nmatrix_3x3_floats:\n", matrix_3x3_floats)
print("Row sums:", row_sums)

# Zadanie 17: Utwórz macierz o rozmiarze 3x4 z dowolnymi liczbami całkowitymi i utwórz macierz z kwadratami tych liczb.
matrix_3x4_any = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
matrix_squared = np.square(matrix_3x4_any)
print("\nZadanie 17:\nmatrix_3x4_any:\n", matrix_3x4_any)
print("Squared matrix:\n", matrix_squared)

# Zadanie 18: Utwórz wektor o rozmiarze 4, wypełnij go losowymi liczbami całkowitymi z zakresu od 1 do 50 i znajdź wektor pierwiastków kwadratowych z tych liczb.
vector_4_large = np.random.randint(1, 51, size=4)
vector_sqrt = np.sqrt(vector_4_large)
print("\nZadanie 18:\nvector_4_large:", vector_4_large)
print("Square roots:", vector_sqrt)
