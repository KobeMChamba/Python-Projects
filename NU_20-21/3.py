# Be sure to upload your work today for your "attendance/participation" grade.
#  I will not be grading your work in detail, simply 1 if submitted, 0 if not.
#  After you finsh the problems below, please work on Assignment 1. 

# For each function, be sure to include:
#  a docstring
#  some valid tests (beyond the 2 provided)

# I have provided 2 asserts for each already. You should uncomment those
#  when you're done to make sure that they pass. Remember that if you
#  run your code, with asserts uncommented, and don't see any output,
#  that means that the test passed.

# We need the following line to allow us to use the List[int] type hint
from typing import List, TypeVar


# Define a function called product_list. It will take as input a list of
#   integers and return the product of those integers. For extra practice,
#   write two versions, one that uses a for loop and another that uses a
#   while loop. 

def product_list(lst: List[int]) -> int:
    product = 1
    for item in lst:
        product *= item
    return product


assert product_list([1, 2, 3, 4]) == 24, "product_list of [1,2,3,4]"
assert product_list([]) == 1, "product_list of []"
assert product_list([1, 0, 3, 4]) == 0, "product_list of [1,0,3,4]"
assert product_list([1, 2, 3, 8]) == 48, "product_list of [1,2,3,8]"


def product_list2(lst: List[int]) -> int:
    product = 1
    for item in lst:
        product *= item
    return product


assert product_list([1, 2, 3, 4]) == 24, "product_list2 of [1,2,3,4]"
assert product_list([]) == 1, "product_list2 of []"
assert product_list([1, 0, 3, 4]) == 0, "product_list of [1,0,3,4]"
assert product_list([1, 2, 3, 8]) == 48, "product_list of [1,2,3,8]"


# write two more valid tests here

# Define a function called find_multiples. It will take as input a list of
#   integers and a number n. It returns the list of numbers from the orignal
#   list that are multiples of n.
#   For extra practice, write two versions, one that uses a for loop and
#   another that uses a while loop. 

def find_multiples(lst: List[int], n: int) -> List[int]:
    multiples_lst = []
    for item in lst:
        if item % n == 0:
            multiples_lst.append(item)
    return multiples_lst


assert find_multiples([1, 4, 5, 6, 7, 8, 9, 10], 5) == [5, 10], "find_multiples test 1"
assert find_multiples([0, 1, 2, 3, 4, 5, 9, 3, 1], 2) == [0, 2, 4], "find_multiples test 2"
assert find_multiples([1, 4, 6, 7, 8, 9], 5) == [], "find_multiples test 1"
assert find_multiples([0, 1, 2, 3, 4, 5, 9, 3, 1], 4) == [0, 4], "find_multiples test 2"
