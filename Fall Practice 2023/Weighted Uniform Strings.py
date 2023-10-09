def weightedUniformStrings(s, queries):
    answers = []
    letter = s[0]
    counter = 1
    letter_dict = {}
    for i in range(1,len(s)-1):
        if s[i] == letter:
            counter = counter + 1
        else: 
            if letter not in letter_dict:
                letter_dict[letter] = counter
            elif counter > letter_dict[letter]:
                letter_dict[letter] = counter
    
    
    for q in queries:
        q_ans = False
        for value in letter_dict.values():
            if divisible(q, value):
                q_ans = True
                break
        answers.append(q_ans)
    
    return answers

            

def divisible(a, b):
    if a % b == 0:
        return True
    return False


 