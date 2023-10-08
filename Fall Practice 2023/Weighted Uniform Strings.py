def weightedUniformStrings(s, queries):
    letter = s[0]
    counter = 1
    letter_dict = {}
    for i in range(1,len(s)-1):
        if letter not in letter_dict:
            letter_dict[letter] = counter
        elif counter > letter_dict[letter]:
            letter_dict[letter] = counter


 