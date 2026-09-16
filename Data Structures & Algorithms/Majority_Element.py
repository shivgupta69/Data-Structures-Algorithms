class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        el = None
        count = 0

        for num in nums:
            if count == 0:
                el = num
                count = 1
            elif num == el:
                count += 1
            else:
                count -= 1
        return el
