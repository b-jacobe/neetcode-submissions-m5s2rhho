class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check for len, if len is even, false
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)