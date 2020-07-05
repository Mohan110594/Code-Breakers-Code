#DFS
#Time comp --> o(V+E)
#space comp --> o(V+E)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        Red=set()
        Black=set()
        
        for i in range(len(graph)):
            if i not in Red and i not in Black and graph[i]:
                Red.add(i)
                
                if self.dfs(graph,Red,Black,i)==False:
                    return False
                    
        return True
                    

        
    
    def dfs(self,graph,Red,Black,index):
        for neig in graph[index]:
            if index in Red:
                if neig not in Red:
                    if neig not in Black:
                        Black.add(neig)
                        if self.dfs(graph,Red,Black,neig)==False:
                            return False
                    
                else:
                    return False
                
            else:
                if neig not in Black:
                    if neig not in Red:
                        Red.add(neig)
                        if self.dfs(graph,Red,Black,neig)==False:
                            return False

                else:
                    return False
                
        return True
        
 #BFS              
 #Time comp --> o(V+E)
 #space comp --> o(V+E)
  
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        neighbors=graph
        Red=set()
        Black=set()
        for index in range(len(neighbors)):
            if index not in Red and index not in Black and neighbors[index]:
                queue=deque([index])


                Red.add(index)

                while len(queue)>0:
                    index=queue.popleft()
                    for neighbour in neighbors[index]:
                        if index in Red :
                            if neighbour not in Red:
                                if neighbour not in Black:
                                    queue.append(neighbour)
                                Black.add(neighbour)
                            else:
                                return False
                        else:
                            if neighbour not in Black:
                                if neighbour not in Red:
                                    queue.append(neighbour)
                                Red.add(neighbour)
                            else:
                                return False
        return True

    
      
            
        