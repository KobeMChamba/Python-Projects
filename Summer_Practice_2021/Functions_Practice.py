def greet_user(first_name, last_name):
    print(f'Hi there, {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user(last_name="Smith", first_name="John")
greet_user("Mary", "Bridges")
# Keyword args should always come after positional args
print("Finish")

# can use return instead of print
def square(number):
    return number * number


# redo emoji converter with a function

def emoji_converter(input):
    words = input.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "🙁",
        "B)": "😎"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

# How to handle exceptions
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be zero.')