#Time --> o(n!)
#space --> o(n)
class Solution:
    def __init__(self):
        self.result=[]
        
    def valid(self,board,row,col):
        # top side
        for i in range(row):
            if board[i][col]==1:
                return False
        
        # up left diagonal 
        
        row1=row-1
        col1=col-1
        while 0<=row1<len(board) and 0<=col1<len(board[0]):
            if board[row1][col1]==1:
                return False
            row1=row1-1
            col1=col1-1
            
        # up right diagonal       
        row1=row-1
        col1=col+1
        while 0<=row1<len(board) and 0<=col1<len(board[0]):
            if board[row1][col1]==1:
                return False
            row1=row1-1
            col1=col1+1
        return True
        
    def backtrack(self,board,row,n):
        
        if row==n:
            # print(board)
            list1=[]
            for i in range(len(board)):
                str1=''
                for j in range(len(board[0])):
                    if board[i][j]==1:
                        str1=str1+'Q'
                    else:
                        str1=str1+'.'
                list1.append(str1)
            self.result.append(list1)
        
        for col in range(n):
            if self.valid(board,row,col):
                board[row][col]=1
                self.backtrack(board,row+1,n)
                board[row][col]=0
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[[0 for i in range(n)]for j in range(n)]
        
        self.backtrack(board,0,n)
        
        return self.result