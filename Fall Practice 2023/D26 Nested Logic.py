# Enter your code here. Read input from STDIN. Print output to STDOUT
d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

if y1 > y2:
    fine = 10000
elif m1 > m2 and y1 == y2:
    fine = 500*(m1-m2)
elif d1 > d2 and m1 == m2 and y1 == y2:
    fine = 15*(d1-d2)
else:
    fine = 0
print(fine)