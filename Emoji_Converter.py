message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "🙁",
    "B)": "😎"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
    # use word as default value so it is ignored if not key value pair
print(output)
