class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check if the rows are valid
        # Check if the columns are valid
        # Check if the 3x3 grid is valid

        rows_dict = collections.defaultdict(set)
        cols_dict = collections.defaultdict(set)
        squares_dict = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                current_val = board[row][col]

                if current_val == ".":
                    continue

                if (
                    current_val in rows_dict[row]
                    or current_val in cols_dict[col]
                    or current_val in squares_dict[row // 3, col // 3]
                ):
                    return False

                rows_dict[row].add(current_val)
                cols_dict[col].add(current_val)
                squares_dict[row // 3, col // 3].add(current_val)

        return True
