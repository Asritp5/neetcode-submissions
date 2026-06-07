class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set=[set() for _ in range(9)]
        col_set=[set() for _ in range(9)]
        
        sub_grid_set=[set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                value=board[i][j]
                if value==".":
                    continue

                if value in row_set[i]:
                    return False

                if value in col_set[j]:
                    return False

                if value in sub_grid_set[(i//3)*3+(j//3)]:
                    return False

                row_set[i].add(value)
                col_set[j].add(value)
                sub_grid_set[(i//3)*3+(j//3)].add(value)

        return True        
                             