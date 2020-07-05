#BFS
#Time comp --> o(V+E)
#space comp --> o(V+E)
from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[False for i in range(n)]
        components=0
        adjList=[[] for i in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        queue=deque([])
        for i in range(n):
            if visited[i]==False:
                components+=1
                queue.append(i)
                
                while len(queue)>0:
                    index1=queue.popleft()
                    for neigh in adjList[index1]:
                        if visited[neigh]==False:
                            visited[neigh]=True
                            queue.append(neigh)
                            
        return components
                
                
 #DFS              
 #Time comp --> o(V+E)
 #space comp --> o(V)
 class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[False for i in range(n)]
        components=0
        adjList=[[] for i in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        for i in range(n):
            if visited[i]==False:
                components+=1
                self.dfs(visited,adjList,i)
                
        return components
        
        
    def dfs(self,visited,adjList,index):
        # print(visited,adjList,index)
        for neigh in adjList[index]:
            if visited[neigh]==False:
                visited[neigh]=True
                self.dfs(visited,adjList,neigh)
                