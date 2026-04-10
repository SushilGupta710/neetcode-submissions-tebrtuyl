class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Solve this problem with Set
        #declearing set because we need to store all the unique value
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        squareSet = [set() for _ in range(9)]

        #iterate the board as it is 2D array we will iterate with nested loop
        for r in range(9):#Outer array
            for c in range(9):#Inner array
                
                #Check first if value is empty then continue and check another value
                if (board[r][c] == '.'):
                    continue
                #To get the index of square
                squareIndex = (r//3)*3 + (c//3)
                #Check all three condition here
                if (board[r][c] in rowSet[r] or
                    board[r][c] in colSet[c] or
                    board[r][c] in squareSet[squareIndex]):
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[squareIndex].add(board[r][c])
        return True


