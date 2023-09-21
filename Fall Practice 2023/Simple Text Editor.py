class TextEditor:
    def __init__(self):
        self.text = ""
        self.operations = []

    def append(self, W):
        self.operations.append(self.text)
        self.text += W

    def delete(self, k):
        self.operations.append(self.text)
        self.text = self.text[:-k]

    def print(self, k):
        print(self.text[k - 1])

    def undo(self):
        if self.operations:
            self.text = self.operations.pop()

def main():
    editor = TextEditor()
    Q = int(input())  # Number of queries

    for _ in range(Q):
        query = input().split()
        operation = query[0]

        if operation == "1":
            editor.append(query[1])
        elif operation == "2":
            editor.delete(int(query[1]))
        elif operation == "3":
            editor.print(int(query[1]))
        elif operation == "4":
            editor.undo()

if __name__ == "__main__":
    main()
