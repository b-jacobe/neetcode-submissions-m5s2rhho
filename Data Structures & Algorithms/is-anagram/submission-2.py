class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        # Aproach 2:
        if len(s) != len(t):
            return False
        count_map_s, count_map_t = {}, {}
        for i in range(len(s)):
            count_map_s[s[i]] = 1 + count_map_s.get(s[i], 0)
            count_map_t[t[i]] = 1 + count_map_t.get(t[i], 0)
        return count_map_s == count_map_t

        