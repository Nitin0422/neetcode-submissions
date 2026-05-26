class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # store temperature value and index of that temperature in a stack

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_temp, stack_indx = stack.pop()
                res[stack_indx] = i - stack_indx
            stack.append((temperature, i))
        
        return res
