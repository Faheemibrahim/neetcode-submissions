class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ya = defaultdict(set)
        xa = defaultdict(set)
        squares = defaultdict(set)

        for y in range(9):
            for x in range(9):
                value = board[y][x]
                if value == ".":
                    continue
# we are doing ya[y] so we can access that row and  column we have 9 rows and 9 columns  

                if (value in ya[y] or 
                value in xa[x] or 
                value in squares[y//3,x//3]):
                    return False
            
                ya[y].add(value)
                xa[x].add(value)
                squares[(y//3,x//3)].add(value)

        return True
    