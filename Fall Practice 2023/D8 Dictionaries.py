EntryCount = int(input())
PhoneBook = {}

def Query(name):
    if PhoneBook.get(name) is None:
        return "Not found"
    else:
        return name + "=" + PhoneBook.get(name)

for _ in range(EntryCount):
    name, number = input().strip().split()
    PhoneBook[name] = number
for _ in range(EntryCount):
    try:
        print (Query(input()))
    except EOFError:
        break