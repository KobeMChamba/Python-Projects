"""Assignment 1

Fill in the following function skeletons (deleting the 'raise NotImplementedError' lines as you go) - descriptions are provided in the PDF, and briefly in the docstring (the triple quote thing at the top of each function).

Some assert statements have been provided - write more of them to test your code!
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built
    in function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    if n < 0:
        n = -1 * n
    return n


assert absolute(-1) == 1, "absolute of -1 failed"
assert absolute(0) == 0, "absolute of -1 failed"
assert absolute(400) == 400, "absolute of -1 failed"


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed
     in number will be positive

     Args:
         n - the number to compute factorial of

     Returns:
         factorial of the passed in number
     """
    nsum = 0
    if n == 0 or n == 1:
        nsum = 1
        return nsum
    else:
        if n > 0:
            nsum = n

    while n > 1:
        nsum = nsum * (n - 1)
        n = n - 1
    return nsum


assert factorial(4) == 24, "factorial of 4 failed"
assert factorial(5) == 120, "factorial of 5 failed"
assert factorial(0) == 1, "factorial of 0 failed"
assert factorial(1) == 1, "factorial of 1 failed"
assert factorial(-4) == 0, "factorial of -4 failed"

T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list,
     starting with the first.

     Args:
        lst - a list of any (constrained by type T to be the same type as the
            returned list)

     Returns:
         a list of every of other item in the original list starting with the first
     """
    returnlst = []
    eocounter = len(lst)
    lstcounter = 0
    while lstcounter < eocounter:
        returnlst.append(lst[lstcounter])
        lstcounter = lstcounter + 2
    return returnlst


assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5], "every_other of [1,2,3,4,5] failed"
assert every_other([1, 2, 3, 4, 5, 6]) == [1, 3, 5], "every_other of [1,2,3,4,5] failed"
assert every_other([1]) == [1], "every_other of [1] failed"
assert every_other([1, 2]) == [1], "every_other of [1] failed"


def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list.
    Cannot use the built in function `sum`.

     Args:
         lst - a list of numbers

     Returns:
         the sum of the passed in list
     """
    result = 0
    slcounter = len(lst) - 1

    while slcounter >= 0:
        result = result + lst[slcounter]
        slcounter = slcounter - 1

    return result


assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
assert sum_list([1, 2, 3, 6]) == 12, "sum_list of [1,2,3,6] failed"
assert sum_list([0, 0, 0, 6]) == 6, "sum_list of [0,0,0,6] failed"
assert sum_list([0, 0, 0, 1]) == 1, "sum_list of [0,0,0,1] failed"
assert sum_list([0, 0, 0, 1, 1000]) == 1001, "sum_list of [0,0,0,1,1001] failed"


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """

    lstsum = sum_list(lst)
    rslt = lstsum / len(lst)
    return rslt


assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
assert mean([1, 2, 3, 4, 5, 6]) == 3.5, "mean of [1,2,3,4,5, 6] failed"
assert mean([0]) == 0, "mean of [0] failed"


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.
    If the list has an even number of values, it computes the mean of the two
    center values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """

    lenlst = len(lst)
    counter = lenlst / 2
    counter = int(counter)
    if lenlst % 2 == 0:
        return (lst[counter - 1] + lst[counter]) / 2
    else:
        return lst[counter]


assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"
assert median([1, 2, 3, 4, 5, 6]) == 3.5, "median of [1,2,3,4,5,6] failed"
assert median([1]) == 1, "median of [1] failed"


def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it,
    knocking out every third name (wrapping around) until only two names are
    left. In other words, when you hit the end of the list, wrap around and keep
    counting from where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd
    first knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on
    Nathan and 'goose' on Sasha - knocking him out and leaving only Nathan and
    Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    counter = 2
    length = len(lst)
    result = lst
    while length > 2:
        length = len(result)
        if length < counter:
            counter = counter - length
        else:
            result.remove(result[counter])
            counter = counter + 2
    return result


names = ["sasha", "nathan", "jennie", "shane", "will", "sara"]
assert duck_duck_goose(names) == ["sasha", "will"], "names asssert failed"

names2 = ['Nathan', 'Sasha', 'Sara', 'Jennie']
assert duck_duck_goose(names2) == ["Nathan", "Jennie"], "names asssert failed"

print("All tests passed!")
