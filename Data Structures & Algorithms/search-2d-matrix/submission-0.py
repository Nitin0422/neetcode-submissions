class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Access each row
        for row in matrix:
            if row[-1] == target:
                return True
            # if the target is less than the last_index of the row, it should lie in that row
            if row[-1] > target:
                left = 0
                right = len(row) - 1

                while left <= right:
                    mid = left + ((right - left) // 2)

                    if row[mid] == target:
                        return True
                    
                    elif row[mid] > target:
                        right = mid - 1
                    
                    elif row[mid] < target:
                        left = mid + 1
                
                return False
        
        return False