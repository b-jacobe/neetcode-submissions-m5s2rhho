# Approach 1: Use a sorted set
# Approach 2: Two Pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # SOLUTION 1:
        # unique = sorted(set(nums))
        # nums[:len(unique)] = unique
        # return len(unique)

        # SOLUTION 2:
        n = len(nums)
        left, right = 0, 0
        while right < n:
            nums[left] = nums[right]
            while right < n and nums[right] == nums[left]:
                right += 1
            left += 1
        return left
    