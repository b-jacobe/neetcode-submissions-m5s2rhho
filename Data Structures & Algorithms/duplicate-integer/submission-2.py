class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set(nums)
        return len(nums) != len(check_set)