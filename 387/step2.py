from collections import Counter, defaultdict


class Solution:
    def firstUniqChar_index(self, s: str) -> int:
        for c in s:
            if s.rindex(c) == s.index(c):
                return s.index(c)
        return -1
    
    def firstUniqChar_Counter(self, s: str) -> int:
        char_to_frequency = Counter(s)
        for index, c in enumerate(s):
            if char_to_frequency[c] == 1:
                return index
        return -1
    
    def firstUniqChar_defaultdict(self, s: str) -> int:
        char_to_frequency = defaultdict(int)
        for c in s:
            char_to_frequency[c] += 1
            
        for index, c in enumerate(s):
            if char_to_frequency[c] == 1:
                return index
        return -1
