#Time comp --> o(V+E)
#space comp --> o(V)
from collections import deque
class Solution(object):
    def __init__(self):
        self.dirs=[[1,0],[-1,0],[0,1],[0,-1]]
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        queue=deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([i,j])

    # if len(queue)==0:
    #         return 0
        level=0
        
        while len(queue)>0:
            size=len(queue)
            
            for i in range(size):
                first,second=queue.popleft()
                for dir in self.dirs:
                    dx=first+dir[0]
                    dy=second+dir[1]
                    if 0<=dx<len(grid) and 0<=dy<len(grid[0]) and grid[dx][dy]==1:
                        grid[dx][dy]=2
                        queue.append([dx,dy])
                        
            level=level+1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        if level==0:
            return 0
        return level-1
                    