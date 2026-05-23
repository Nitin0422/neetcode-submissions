class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num, count in freq.items():
            buckets[count].append(num)

        res = []

        for i in range(len(buckets) - 1, -1, -1):
            num_list = buckets[i]

            for num in num_list:
                res.append(num)

                if len(res) == k:
                    return res
