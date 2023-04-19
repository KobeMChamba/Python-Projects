# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    t = input()
    if t[0] == 'S':
        for char in range(t):
            if t[char].isupper():
                new_s = ""
                if t[char].isupper():
                    new_s += " " + t[char]
                else:
                    new_s += t[char]
        if t[2] == 'M':
            new_s = new_s[:-2]
        elif t[2] == 'C' or t[2] == 'V':
            new_s = new_s.lower()
    else:
        ##t[0] == C:
        if t[2] == 'V' or t[2] == 'M':
        ##take out space and make letter after space uppercase
            words = t.split()
            new_s = words[0] + ''.join(word.capitalize() for word in words[1:]))
            if t[2] == 'M':
                new_s = new_s + "()"
        if t[2] == C:
            words = t.split()
            new_s = words[0] + ''.join(word.capitalize() for word in words)
            
    print(new_s)