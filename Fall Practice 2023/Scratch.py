# Define the size of the 2D array
N = 3  # Number of rows
M = 2  # Number of columns

# Create a 2D array where each element is a list containing a tuple and a list of tuples
array_2d = []
for i in range(N):
    row = []
    for j in range(M):
        # Define a tuple and a list of tuples for each element
        element_tuple = (i, j)
        element_list_of_tuples = [(i, j), (i+1, j+1)]
        element = (element_tuple, element_list_of_tuples)
        row.append(element)
    array_2d.append(row)

# Access an element and its components
element = array_2d[1][0]
tuple_value, list_of_tuples = element
print("Tuple:", tuple_value)
print("List of Tuples:", list_of_tuples)

# Print the entire 2D array
for row in array_2d:
    for element in row:
        print(element)
