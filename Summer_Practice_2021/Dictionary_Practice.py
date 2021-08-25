from typing import Dict, Union

customer: Dict[str, Union[str, int, bool]] = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# print(customer["name"])
# print(customer.get("birthdate", "Jan 1 1980"))
# the latter is better as it returns None rather than an error when the key is incorrect.
# You can also add a default value.
(customer["name"]) = "Jack Smith"
# print(customer["name"])
# can also update key value pairs

customer["birthdate"] = "Jan 31 1980"
# print(customer.get("birthdate", "Jan 1 1980"))
# can add key value pairs

# Phone number exercise
phone = input("Phone: ")
# we need to map each digit to a word
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)