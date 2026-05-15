class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collector = []
        matched_indices = []

        print(len(strs))
        if len(strs) <= 1:
            return [strs]

        for i in range(len(strs)):
            if i in matched_indices:
                continue
            inner_arr = []
            p1 = strs[i]
            inner_arr.append(p1)
            for j in range(i+1, len(strs)):
                p2 = strs[j]

                if sorted(list(p1)) == sorted(list(p2)):
                    inner_arr.append(p2)
                    matched_indices.append(j)

            collector.append(inner_arr)

        return collector