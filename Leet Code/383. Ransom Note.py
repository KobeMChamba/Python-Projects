class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a list to store the counts of each letter (26 letters in total)
        mag_count = [0] * 26
        
        # Increment counts based on letters in magazine
        for letter in magazine:
            mag_count[ord(letter) - ord('a')] += 1
        
        # Decrement counts based on letters in ransomNote
        for letter in ransomNote:
            index = ord(letter) - ord('a')
            mag_count[index] -= 1
            if mag_count[index] < 0:
                return False
        
        return True

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         mag_dict = {}
#         for letter in magazine:
#             if letter not in mag_dict:
#                 mag_dict[letter] = 1
#             else:
#                 mag_dict[letter] = mag_dict[letter] + 1
#         for letter in ransomNote:
#             if letter not in mag_dict:
#                 return False
#             else:
#                 mag_dict[letter] = mag_dict[letter] - 1
#             if mag_dict[letter] == 0:
#                 del mag_dict[letter]
#         return True
