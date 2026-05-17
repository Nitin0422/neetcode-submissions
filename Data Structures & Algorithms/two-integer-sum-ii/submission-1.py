class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            # Check with respect to the index
            for j in range(len(numbers)):
                if numbers[i] == numbers[j]:
                    continue

                if target == numbers[i] + numbers[j]:
                    return [i + 1, j + 1]
