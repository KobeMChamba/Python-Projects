class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w = defaultdict(list)
        for s in strs:
            w[''.join(sorted(s))].append(s)
        return list(w.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams_dict = {}
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             if sorted_word not in anagrams_dict:
#                 anagrams_dict[sorted_word] = [word]
#             else:
#                 anagrams_dict[sorted_word].append(word)
#         return list(anagrams_dict.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # w = defaultdict(list)
        # for s in strs:
        #     char_count = [0]*26
        #     for char in s:
        #         char_count[ord(char)-ord("a")] += 1
        #     w[tuple(char_count)].append(s)
        
        # return list(w.values())