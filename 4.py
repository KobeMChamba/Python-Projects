#Be sure to upload your work today for your "attendance/participation" grade.
#  I will not be grading your work in detail, simply 1 if submitted, 0 if not.
#  After you finsh the problems below, please work on Assignment 1.

#I have provided 2 asserts for each already. You should uncomment those
#  when you're done to make sure that they pass. Remember that if you
#  run your code, with asserts uncommented, and don't see any output,
#  that means that the test passed.

# Recall the slice notation list[start:end:step]

#Define a function called crop_list. It will take as input a list named lst of length greater than 4. 
# It returns a new list, build form lst, but discarding the first and last two elements. 
def crop_list(lst:list)->list:
    newlst = lst[2:(len(lst)-2)]
    return newlst

assert crop_list([1, 2, 3, 4, 5]) == [3], "cropping 12345"
assert crop_list(["North", "Western", "Computer", "Science", "Departmental", "Affairs"]) == ["Computer", "Science"], "cropping Comp Sci"
assert crop_list([1, 2, 3, 4, 5, 6]) == [3, 4], "cropping 123456"
assert crop_list([1, 2, 3, 4, 5, 6, 7]) == [3, 4, 5], "cropping 123456"
assert crop_list([]) == [], "empty"

#Define a function called backward_hop. It will take as input a list named code.
#   It returns a new list, built from the original string, but starting backwards 
#   counting every second item. For example, backward_hop(['3','t','2','a','1','c'])
#   will return ['c','a','t'].
def backward_hop(code:list)-> list:
    newlst = code
    newlst.reverse()
    counter = 1
    while counter < len(newlst):
        newlst.pop(counter)
        counter = counter + 1

    return(newlst)


assert backward_hop(['3','t','2','a','1','c']) == ['c','a','t'], "backward hop of cat"
assert backward_hop(['e','i','t','u','a','y','g','t','r','r','e','e','t','w','a','q','w'])==['w','a','t','e','r','g','a','t','e'], "backward hop of watergate"
assert backward_hop([]) ==[], "backwards hop of empty list"
assert backward_hop([1]) ==[1], "backwards hop of one item list"

print("All asserts passed!!!!")
