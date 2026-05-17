class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the provided array in to set
        set_nums = set(nums)

        max_count = 0
        for num in set_nums:
            # Check if it has a left neighbour
            if (num - 1) in set_nums:
                continue # not the start of a sequence
            
            internal_count = 1
            current = num
            while (current + 1) in set_nums:
                current +=1
                internal_count += 1
            
            if max_count < internal_count:
                max_count = internal_count
        return max_count
