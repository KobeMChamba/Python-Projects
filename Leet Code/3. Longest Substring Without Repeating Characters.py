class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)
        
        return max_length
        
        # Better solution
        char_dict = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_dict and char_dict[s[right]] >= left:
                left = char_dict[s[right]]+1
                char_dict[s[right]] = right
            else:
                char_dict[s[right]] = right
                max_length = max(max_length, right - left + 1)
        return max_length