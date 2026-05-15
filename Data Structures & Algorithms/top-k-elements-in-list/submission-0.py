class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            bucket[count].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for number in bucket[i]:
                res.append(number)

                if len(res) == k:
                    return res         