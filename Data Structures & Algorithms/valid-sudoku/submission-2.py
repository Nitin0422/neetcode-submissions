class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # store for rows, cols and squares
        row_dict = collections.defaultdict(set)
        col_dict = collections.defaultdict(set)
        square_dict = collections.defaultdict(set)

        # loop throught the board
        for i in range(len(board)):
            for j in range(len(board[i])):
                current_value = board[i][j]

                if current_value == ".":
                    continue

                # for values in rows, cols and squares
                if (
                    current_value in row_dict[i]
                    or current_value in col_dict[j]
                    or current_value in square_dict[i // 3, j // 3]
                ):
                    return False

                row_dict[i].add(current_value)
                col_dict[j].add(current_value)
                square_dict[i // 3, j // 3].add(current_value)

        return True
