# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_dict = {}
for i in range(n):
    data = input()
    values = data.split()
    name = values[0]
    num = values[1]
    phone_dict[name] = num
    #print(name)
    #print(num)
    #print(phone_dict)
for i in range(n):
    name = input()
    #print(name)
    if name in phone_dict.keys():
        print(name+"="+phone_dict[name])
    else:
        print("Not found")
    