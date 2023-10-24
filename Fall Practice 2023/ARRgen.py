import random

# Define the size of the arrays
m = 5

# Generate two arrays of random numbers between -8 and 8
array1 = [random.randint(1, 1) for _ in range(m)]
array2 = [random.randint(1, 1) for _ in range(m)]

# Create a 2D array of their products
product_array = [[array1[i] * array2[j] for j in range(m)] for i in range(m)]

# Print the original arrays and the product array
print("Arr1 = ", array1)
print("Arr2 = ", array2)
print("ProdArr = [")
for row in product_array:
    print("    [", end='')
    for elem in row:
        print(elem, end=', ')
    print("],")
print("]")
