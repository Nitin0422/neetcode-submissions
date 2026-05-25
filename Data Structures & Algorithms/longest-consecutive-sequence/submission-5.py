class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)

        res = 0

        for num in uniq_nums:
            if (num - 1) in uniq_nums:  # it cannot be start of a sequence
                continue

            seq_count = 1
            current = num
            # check if the seq exists
            while (current + 1) in uniq_nums:
                current += 1
                seq_count += 1

            res = max(res, seq_count)
        return res
