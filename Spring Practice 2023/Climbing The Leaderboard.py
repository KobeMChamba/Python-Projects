#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
'''
def dense_ranking(lst):
    rank = 1
    rank_dict = {}
    for i in range(len(lst)):
        if i > 0 and lst[i] != lst[i-1]:
            rank += 1
        rank_dict[lst[i]] = rank
    return rank_dict

def climbingLeaderboard(ranked, player):
    # Write your code here
    #ranked.extend(player)   # add the elements of b to a
    #ranked.sort()      # sort the combined list
    #dense_ranks = dense_rank(ranked)
    list = []
    new_rank = ranked
    for score in player:
        new_rank = new_rank+[score]
        #print(new_rank)
        new_rank.sort(reverse=True)
        print(new_rank)
        dense_ranks = dense_ranking(new_rank)
        #print(dense_ranks)
        list.append(dense_ranks[score])
    return list
'''
def climbingLeaderboard(ranked, player):
    ans=[]
    ranked = sorted(list(set(ranked)), reverse = True)
    for p in player:
        first = 0
        last = len(ranked)-1
        while first <= last:
            found = 0
            center = first + int((last - first)/2)
            if p < ranked[center]:
                first = center + 1
            elif p > ranked[center]:
                last = center - 1
            else:
                found = 1
                ans.append(center + 1)
                break
        if not found:
            if p > ranked[center]:
                ans.append(center + 1)
            else:
                ans.append(center + 2)
    return ans




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
