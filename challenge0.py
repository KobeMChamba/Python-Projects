# CODE BY KATE COMPTON, NORTHWESTERN UNIVERSITY CS DEPT
# Copyright 03/31/2021
# Released under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)


# This line imports the CSV library, 
# a built-in Python library that can open 
# and process CSV data files in a convenient way
# The next one imports a library that makes random numbers
# After this line, we will have a "csv" and "random" object with useful methods
import csv
import random

# Indexes for each of the kinds of data
# Lining up the numbers doesn't do anythin here
# It just makes it more readable, 
# and easier to see if I have missed a number
# Notice that in python, we don't need a datatype to define a variable ("int x"),
#  we just name the variable, and set it equal to a value

index_first = 1
index_last = 2
index_bio = 3
index_year = 4
index_major = 5
index_major2 = 6
index_drink = 7
index_emoji_weird = 8
index_emoji_fav = 15  # this one was out of order, oops
index_house = 9
index_house_stuff = 10
index_birthday = 11
index_food = 12
index_idea_internet = 13
index_idea_mine = 14

# These are the survey options, we can use these later
house_options = ["in a tiny beachside shack", "in a sprawling luxury mansion", "in an ancient castle full of secrets",
                 "in a downtown penthouse", "in a remote cabin", "in a space station", "in an underground volcano lair",
                 "on a farm", "on a yacht"]
house_stuff_options = ["my best friends", "my family", "my whole team", "so many dogs", "so many cats",
                       "too many plants", "a dragon of questionable allegiance", "all my craft supplies",
                       "all my books", "all my sneakers", "a mysterious yet attractive stranger with a sinister past",
                       "an extremely powerful computer", "WIFI"]

# This is a variable to hold the  name of our file,
#  It's relative to where we run Python from
# If it were in a folder, we could specify the path, too 
#   e.g "/my_folder/a0_files/responses.csv"
filename = 'challenge0-responses.csv'


# This is a class
# It's a convenient template for holding information 
#   as long as each "instance" of the class (each student) 
#   needs the same kind of information
# Classes start with a capital letter, not because they have to, 
#   but because it makes it easier for us humans to remember 
#   that its a class wehn we use it later
class Student:

    # Given a list of data about a student, create that student
    # This is a special method called a "constructor" that initializes the instance
    # It gets called automatically when the instance is created
    def __init__(self, data):
        # Try printing out the data
        # It should be a list with lots of strings
        # print("Student data: ", data)

        # In all these lines, I'm copying the information
        #  from the "data" list into the Student instance
        # After this, I'll be able to say "my_student.first" or "my_student.bio"
        #   to get the information out again
        self.first = data[index_first]
        self.last = data[index_last]
        self.bio = data[index_bio]
        self.year = data[index_year]
        self.food = data[index_food]
        self.drink = data[index_drink]
        self.major = data[index_major]
        self.major2 = data[index_major2]
        self.emoji_weird = data[index_emoji_weird]
        self.emoji_fav = data[index_emoji_fav]
        self.house = data[index_house]
        self.house_stuff = data[index_house_stuff]
        self.birthday = data[index_birthday]
        self.idea_internet = data[index_idea_internet]
        self.idea_mine = data[index_idea_mine]

    # This method implements a way for this instance to turn into a string when we need it to
    # like when we say f"{student} went to the beach"
    def __str__(self):
        # "self" is the student instance
        return f"{self.first} {self.last}"


# We will start with an empty list of students, and add to it as we read the file
all_students = []

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# LOAD STUDENTS !!!

# This line opens up the file at the filename location
# and gives us a reference to the now-readable file: a variable named "csv_file"
with open(filename, encoding="utf8") as csv_file:
    # In this line, we use the "csv" object we imported above to process the csv_file
    # into several rows of data
    # (More about Python and CSV files https://realpython.com/python-csv/)

    data_rows = csv.reader(csv_file, delimiter=',')

    # If you print it, you'll see that it is a *list of lists*
    # e.g.: [[some stuff, ..., ..., ...],[more stuff, ..., ..., ...]]
    # Its a lot of information to read,
    # but you can comment this line on and off to look at it whenver you want
    # print(data_rows)

    # line_count is a varible
    line_count = 0

    # We will see this "for x in some_list:" pattern a lot in Python
    # If we have a list of things, it allows us to *iterate* over them one at a time
    for row in data_rows:
        # Once inside the loop, we can ignore the  "data_rows" list, and just look at "row"

        if line_count == 0:
            # If this is the first row, print out the headings
            # uncomment this line to see all the headings
            # print(f'Column names are {", ".join(row)}')

            # Python needs to have at least one real line of code after every if-statement
            # If we comment out the print statement above, we won't have one
            # so "pass" is a kinda silly command that tells Python to keep going here
            pass
        else:
            # Each row is a different student, so we use the class Student to create a new
            # student instance with this row as the data
            new_student = Student(row)
            # print(f"student #{line_count} processed: {new_student}")

            # Then we add the new student to the list
            all_students.append(new_student)

        # add one to line count each time
        line_count += 1
    # we can still

    print(f'Finished processing {line_count} lines.')
    print(f'There are {len(all_students)} students.')

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# LOOK AT STUDENTS WITH FUNCTIONS !!!

# -------------------------------------------------------------------------------------------
# BASIC EXAMPLES

# list all the students
for student in all_students:
    print(student, ":", student.major, ",", student.major2)


# list all the students who would have plants
# for student in all_students:
# 	if "too many plants" in student.house_stuff:
# 		print(student.first, student.last, "would have plants in", student.house)


# -------------------------------------------------------------------------------------------

def emoji_roundup():
    # Add all the emoji to a list and print it
    all_emoji = []
    no_emoji = 0
    for student in all_students:

        # Store the emoji value in this variable
        # using well-named variables makes your code easier to read
        my_emoji = student.emoji_fav

        # Is this an emoji, or an empty string?
        if len(my_emoji) > 0:
            # this emoji exists!
            # Add it to the emoji list
            all_emoji.append(my_emoji)
        else:
            # oops, no emoji
            no_emoji += 1

    print(all_emoji)
    print(no_emoji, "students have no favorite emoji")


# Run the emoji function
# emoji_roundup()


# Who likes coffee or tea?
def drink_survey():
    coffee = 0
    tea = 0
    other_drink = 0
    for student in all_students:
        # Convert the drink to lowercase so we won't be fooled if they have "Coffee" or "cOfFeE"
        my_drink = student.drink.lower()
        if "coffee" in my_drink or "espresso" in my_drink or "latte" in my_drink:
            coffee += 1
        elif "tea" in my_drink or "chai" in my_drink:
            tea += 1
        else:
            other_drink += 1

    print("COFFEE:\t", coffee)
    print("TEA:\t", tea)
    print("OTHER:\t", other_drink)


# Run the drink survey
# drink_survey()


def house_graph():
    # This is a Python dictionary!
    # its a data structure that lets us store values and look them up with string keys
    # like {a:0, b: 5, c: 10}
    results = {}

    # iterate through the student list
    for student in all_students:

        # Have we encountered this option before?
        # If not, add it to the results (with a score of 0)
        house_choice = student.house
        if house_choice not in results:
            results[house_choice] = 0
        results[house_choice] += 1

    # Wait...we can iterate over Dictionaries, too!
    for house_choice in results:
        score = results[house_choice]

        # print out the option (and pad it with spaces so it lines up nicely)
        print(house_choice.rjust(38, ' '), ":", score)
    # What does this line do?
    # print(house_choice.rjust(38, ' '), ":", "■"*score)


# Run the house graph
# house_graph()


# Select a random student
# to do that, we need a random index from 0 to the number of students (minus 1)
# We can use random.randint for that, which gives us a random integer
def get_random_student():
    student_index = random.randint(0, len(all_students) - 1)
    student = all_students[student_index]
    return student


# A quiz to practice names
def quiz():
    for i in range(0, 20):
        # Select 4 random students
        # First shuffle all the students.  shuffle is built into the random library!
        random.shuffle(all_students)
        # Take the first 4 students from the shuffled pile
        quiz_students = all_students[0:4]

        print("\nROUND", i)

        choice_count = 4
        hint_number = choice_count + 1

        # Pick the student who will be our right answer
        right_answer = random.randint(0, choice_count - 1)
        right_student = quiz_students[right_answer]

        # for each student in our selected set, print them out
        # Here, we *need* to use range, because we need to label each student with a number
        # if we used "for student in quiz_students" we wouldn't know what numbers to use
        for j in range(0, len(quiz_students)):
            student = quiz_students[j]
            print(j, ": ", str(student))
        print(hint_number, ": ", "hint")

        print(f"'{right_student.bio}'")

        # Read the player's input and convert it to an int
        choice = int(input(""))

        # Until they get it right, keep asking
        while choice != right_answer:

            # Are they asking for a hint?
            if choice == hint_number:
                hints = [f"my favorite drink is {right_student.drink}",
                         f"my favorite emoji is {right_student.emoji_fav}",
                         f"my favorite emoji is {right_student.emoji_fav}"]
                hint_index = random.randint(0, len(hints) - 1)

                # Print that hint!
                print(hints[hint_index])
            else:
                wrong_student = quiz_students[choice]
                print(f"Nope, not {wrong_student}, they are '{wrong_student.bio}'")

            # Read more input
            choice = int(input(""))

        print(f"Right! {right_student} is '{right_student.bio}'")
        print(f"also they like {right_student.drink} and {right_student.food}")


# uncomment to play the quiz
# quiz()

def virtual_northwestern():
    # A "while" loop!
    # We use these when we *don't know how many times a loop should run*
    # Here, I want it to run forever, so it runs as long as... True is true (forever)
    # ("while True: i love you" is a nice thing for python programmers to say to each other)
    while True:
        student = get_random_student()
        classmate = get_random_student()

        # What is this student doing right now?
        # pick a random activity with the same formula we used above!
        activities = [f" drinks {student.drink}", f" finishes {student.major} homework",
                      f" studies some {student.major2}", f" goes to get {student.food}", f" hangs out with {classmate}"]
        activity_index = random.randint(0, len(activities) - 1)
        activity = activities[activity_index]
        print(str(student) + activity)


# Run the virtual northwestern simulation
# it runs forever, hit CTRL-C to escape
# virtual_northwestern()

def first_name_find():
    print("The following students have names that start with 'S'")
    for student in all_students:
        if student.first[0] == "s" or student.first[0] == "S":
            print(student)


first_name_find()


def longest_name_find():
    longest_name = ""
    for student in all_students:
        if len(student.last) > len(longest_name):
            longest_name = student.last
    print(longest_name, "is the longest last name")


longest_name_find()


# a method to determine if this student has the same birthday as the other student
def has_same_birthday(self, student):
    return self.birthday == student.birthday


def share_birthday():
    share_bd = False
    for student1 in all_students:
        for student2 in all_students:
            if has_same_birthday(student1, student2):
                share_bd = True
    print("It is", share_bd, "that students share birthdays.")


share_birthday()


def april_or_may():
    print("The following students have a birthday in April or May")
    for student in all_students:
        if "04/" in student.birthday or "05/" in student.birthday:
            print(student.first, student.last)


april_or_may()
