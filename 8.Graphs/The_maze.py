#Time comp --> o(mn)
#space comp --> o(mn)

from collections import deque
class Solution:
    def __init__(self):
        self.dirs=[[1,0],[-1,0],[0,1],[0,-1]]
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if len(maze)==0:
            return False
        
        visited=[[False for i in range(len(maze[0]))]for j in range(len(maze))]
        
        queue=deque([[start[0],start[1]]])
        
        visited[start[0]][start[1]]=True
        
        while len(queue)>0:
            first,second=queue.popleft()
            
            if first==destination[0] and second==destination[1]:
                return True
                
                
            for dir in self.dirs:
                first1=first+dir[0]
                second1=second+dir[1]
                
                while 0<=first1<len(maze) and 0<=second1<len(maze[0]) and maze[first1][second1]==0:
                    first1=first1+dir[0]
                    second1=second1+dir[1]
                 
                first1=first1-dir[0]
                second1=second1-dir[1]
                
                if visited[first1][second1]==False:
                    visited[first1][second1]=True
                    queue.append([first1,second1])
                    
        return False
        
                
            