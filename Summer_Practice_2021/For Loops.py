for item in ['Mosh', 'John', 'Sarah']:
    print(item)
for item in range(10):
    print(item)
    #prints 0-9
for item in range(5,10,2):
    #prints 5 to 10 using 2 steps
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
