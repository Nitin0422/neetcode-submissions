class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums)) 

        prefixed_prod = 1
        for i in range(len(nums)):
            res[i] = prefixed_prod
            prefixed_prod *= nums[i]
        
        print(res)

        postfixed_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfixed_prod
            postfixed_prod *= nums[i]
        
        print(res)

        return res
