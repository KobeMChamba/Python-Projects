# Enter your code here. Read input from STDIN. Print output to STDOUT

s = ""
#last done action
lda = 0

for _ in range(int(input())):
    val = list(input().split())
    if val[0] == "1":
        #if 1, append
        s = s + val[1]
        lda = lda + 1
    elif val[0] == "2":
        #if 2, delete the last k characters of S
        s = s[:(len(s)-val[1])]
        lda = lda + 1
    elif val[0] == "3":
        #if 3, print the kith character of S
        print(s[val[1]-1])
        lda = lda + 1
    elif val[0] == "4":
        #undo the last not previously undone operation of type 1 or 2
        
        