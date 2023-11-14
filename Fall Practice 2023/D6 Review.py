# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())

while num > 0:
    #print(num)
    even = ""
    odd = ""
    string = input()
    for i in range(len(string)):
        if i % 2 == 0:
            even = even + string[i]
        else:
            odd = odd + string[i]
    num -= 1
    print(even + " " + odd)
    #print(even)