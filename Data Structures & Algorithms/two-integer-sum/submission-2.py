class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped_nums = {}

        for i, num in enumerate(nums):
            difference = target - num 

            if difference in mapped_nums:
                return [mapped_nums[difference], i]
            
            mapped_nums[num] = i
