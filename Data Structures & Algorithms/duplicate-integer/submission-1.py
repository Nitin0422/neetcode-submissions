class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        count = 0
        last_value = None
        for i, num in enumerate(nums):
            if last_value == None:
                last_value = num
                continue
            
            if last_value == num:
                return True
            
            last_value = num
        
        return False
