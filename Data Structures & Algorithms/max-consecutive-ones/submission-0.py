class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # create max_counter
        # iterate via for loop and count instance of 1
        # set max_counter, reset iterator if 0
        # return max_counter
        # i.e. nums = [1,1,1,0,1,1] --> 3
        max_counter = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter+=1
                if max_counter < counter:
                    max_counter = counter
            else:
                counter = 0
        return max_counter
        