class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collector = {}

        for num in nums:
            collector[num] = 1 + collector.get(num, 0)

            if collector[num] > 1:
                return True

        return False
