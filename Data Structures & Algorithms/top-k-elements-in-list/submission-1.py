class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I nitialize empty array of arrays of size len(nums)
        # the index of the array will determine the count
        # the values indicate the numbers in the original array
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
