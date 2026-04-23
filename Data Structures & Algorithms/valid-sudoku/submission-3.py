class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #So solve this we need three parameter 
        rowSet = defaultdict(set) #store rows 0:{values}
        colSet = defaultdict(set) #store cols 0:{values}
        squareSet=defaultdict(set) #store box (0,0):{values}
        #we know the box will be range 9
        for r in range(9):
            for c in range(9):
                #first we need to just check or exclude '.' value
                if board[r][c] == '.':
                    continue
                
                #Before adding any value we need to check if values exist in set's then return False from here directly
                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in squareSet[(r//3,c//3)]:
                    return False

                
                #Let's add the values in sets
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                #Here is the trick to add valye in square
                squareSet[(r//3,c//3)].add(board[r][c])
                #here r//3 and c//5means we need to get roundoff reminder value
                #eg r=8, c=7 ==> r=8//3 =2(get the remender), c=7//3=2(get the remender)
        #At last if every thing is valid we need to return True from here
        return True