class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Solving this problem using defaultDict of Set as Easy way
        rowSet = collections.defaultdict(set)
        colSet = collections.defaultdict(set)
        squareSet=collections.defaultdict(set) #to get the square value use (r//3,c//3)

        #Now iterate the 2D array board with nested loop
        for r in range(9):
            for c in range(9):

                #First check if in board there is empty value exist
                if(board[r][c] == '.'):
                    continue
                
                #2nd check all the condition if value is duplicate then return false
                #clean Code to get the key of squareSet
                squareIndex = (r//3),(c//3)
                if(board[r][c] in rowSet[r] or
                   board[r][c] in colSet[c] or
                   board[r][c] in squareSet[squareIndex]):
                   return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[squareIndex].add(board[r][c])
        return True
        
        