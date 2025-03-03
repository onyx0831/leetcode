from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_frequency = Counter(s)
        for index, c in enumerate(s):
            if char_to_frequency[c] == 1:
                return index
        return -1 # not found
