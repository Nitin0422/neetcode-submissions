class Solution:
    def trap(self, height: List[int]) -> int:
        # Calculate the maxleft and the max right for each of the element in the array
        max_left = []
        max_right = []

        max_h = 0
        for i in range(len(height)):
            max_left.append(max_h)
            if height[i] > max_h:
                max_h = height[i]
              
        max_h = 0
        for j in range(len(height) -1, -1, -1):
            max_right.append(max_h)
            if height[j] > max_h:
                max_h = height[j]
        
        max_right = list(reversed(max_right))
        
        total_water = 0

        for i, pillar in enumerate(height):
            total_water += max(0, (min(max_left[i], max_right[i]) - pillar))

        return total_water
            
