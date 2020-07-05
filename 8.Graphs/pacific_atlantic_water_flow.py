#DFS
#Time comp --> o(mn)
#space comp --> o(mn)
class Solution:
    def __init__(self):
        self.dirs=[[0,1],[1,0],[0,-1],[-1,0]]
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if len(matrix)==0:
            return []
        
        # Maintain two separate arrays to check if any cell can be reached from the given rivers
        pacific=[[0 for j in range(len(matrix[0]))]for i in range(len(matrix))]
        
        atlantic=[[0 for j in range(len(matrix[0]))]for i in range(len(matrix))]
        
        result=[]
        
        # Pacific is at row0 and col0
        # Atantic is at maxrow and maxcol
        
        
        for i in range(len(matrix)):
            pacific[i][0]=1
            atlantic[i][len(matrix[0])-1]=1
            
        
            
        for j in range(len(matrix[0])):
            pacific[0][j]=1
            atlantic[len(matrix)-1][j]=1
                
    # so doing dfs on the elements row0 and row=len(matrix)-1 to see if water can be flown into the matrix
        
        for col in range(len(matrix[0])):
            
            self.dfs(matrix,0,col,pacific)
            
            self.dfs(matrix,len(matrix)-1,col,atlantic)
        
        # again doing dfs on the elements in  col=len(matrix[0])-1 and col=0 to see if water can be flown into the matrix
        for row in range(len(matrix)):
            self.dfs(matrix,row,0,pacific)
            self.dfs(matrix,row,len(matrix[0])-1,atlantic)
        
        # Intersection of cells where both pacific and atlantic meets
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific[i][j]==1 and atlantic[i][j]==1:
                    result.append([i,j])
                    
        return result
        
    def dfs(self,matrix,row,col,ocean):
        
        ocean[row][col]=1
        
        for dir in self.dirs:
            row1=row+dir[0]
            col1=col+dir[1]
            if 0<=row1<len(matrix) and 0<=col1<len(matrix[0]) and ocean[row1][col1]==0 and matrix[row1][col1]>=matrix[row][col]:
                self.dfs(matrix,row1,col1,ocean)
        
        