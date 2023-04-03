class TextEditor:
    def __init__(self,S=''):
        self.S=S
        self.undo_list = []
        
    def append(self, w):
        self.undo_list.append(self.S)
        self.S += w
    def delete(self, k):
        self.undo_list.append(self.S)
        self.S = self.S[:-k]
        
    def print(self, k):
        print(self.S[k-1])
        
    def undo(self):
        self.S = self.undo_list.pop()
        
S = TextEditor()
n = int(input())
for _ in range(n):
    t = input()
    if t == '4':
        S.undo()
    else:
        digit, value = t.split()
        if digit == '1':
            S.append(value)
        if digit == '2':
            k = int(value)
            S.delete(k)
        if digit == '3':
            k = int(value)
            S.print(k)