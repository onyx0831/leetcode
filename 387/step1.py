
class Solution:
    def firstUniqChar(self, s: str) -> int:

        appearance_dict = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        index_dict = {chr(c): 10 ** 6 for c in range(ord('a'), ord('z') + 1)}
        len_s = len(s)

        for i in range(len_s):
            target = s[i]
            appearance_dict[target] += 1
            index_dict[target] = min(i, index_dict[target])
        
        one_apper_list = [key for key, value in appearance_dict.items() if value == 1]

        if one_apper_list:
            index_value = 10 ** 6
            for c in one_apper_list:
                index_value = min(index_dict[c], index_value)
            return index_value
        else:
            return -1

