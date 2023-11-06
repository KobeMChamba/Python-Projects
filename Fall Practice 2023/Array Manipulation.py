def arrayManipulation(n, queries):
    l = []
    for a, b, k in queries:
        l.append((a-1, k))
        l.append((b, -k))
    l.sort()
    print("l: ", l)
    curr_sum = 0
    best = -1
    curr_index = 0
    for idx, val in l:
        if idx != curr_index:
            best = max(best, curr_sum)
            curr_index = idx
        curr_sum += val
    return best

n = 5  # Replace with your desired value of 'n'

queries = [
    (1, 2, 50),
    (2, 5, 30),
    (3, 4, 10)
    # Add more queries as needed
]

result = arrayManipulation(n, queries)
print("Maximum value:", result)
