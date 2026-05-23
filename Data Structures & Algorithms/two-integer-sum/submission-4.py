class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        # The difference of each element from the target will add up to target

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hash_set:
                return [hash_set[diff], i]
            
            hash_set[nums[i]] = i
