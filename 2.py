# Please note that this work will not be graded. These are practice problems.
#  In future classes, you will submit your daily practice problems
#  for attendance/participation credit. Please help each other within
#  your group. Feel free to share screen to show others what you are doing
#  to help each other with debugging. I encourage you to stay positive and
#  avoid phrases like "this is easy" as this is usually discouraging to
#  students who are stuck or encountering bugs. 
# HAPPY CODING!!!!

# I have provided you with two challenges below. These will test your
#  understanding of the modules that you did before class today.
#  Feel free to look back at the notes for help. In particular, in module
#  2, the file "2 - Functions.py" would be very helpful. I will post
#  solutions after class. 

# For each function, be sure to include:
#  a docstring
#  type hints on inputs and return type
#  some valid tests (beyond the 2 provided)

# I have provided 2 asserts for each already. You should uncomment those
#  when you're done to make sure that they pass. Remember that if you
#  run your code, with asserts uncommented, and don't see any output,
#  that means that the test passed.

# Define a function called count_change. It will take as input 4 integers
#  that represent the number of quarters, dimes, nickels and pennies that
#  we have. The function should calculate the return the dollar value,
#  as a float, of that combination of coins. 

# DEFINE YOUR count_change FUNCTION HERE
def count_change(q, d, n, p: int) -> float:
    q = q * 25
    d = d * 10
    n = n * 5
    dollars = (q + d + n + p) / 100
    return dollars


assert count_change(2, 0, 0, 1) == 0.51, "count_change of 2, 0, 0, 1"
assert count_change(4, 10, 20, 100) == 4.0, "count_change of 4,10,20,100"
assert count_change(0, 0, 0, 0) == 0, "count_change of 0, 0, 0, 0"
assert count_change(0, 2, 2, 0) == .30, "count_change of 0, 0, 0, 0"



# Define a function called is_odd. It will take as input an integer x and
#  return True if x is odd, False otherwise.

# DEFINE YOUR is_odd FUNCTION HERE
def is_odd(x: int) -> bool:
    """
    ARGS: integer
    RETURNS: true if integer is odd
    """

    if x % 2 == 0:
        return False
    else:
        return True


assert is_odd(5) == True, "is_odd of 5"
assert is_odd(4) == False, "is_odd of 4"
assert is_odd(40) == False, "is_odd of 4"
