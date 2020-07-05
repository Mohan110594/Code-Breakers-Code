#BFS

#Time comp --> o(v+E)
#space comp --> o(v)

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        outdegree=[None for i in range(len(graph))]
        result=[]
        
        # finding the outdegree for every node in the graph
        for i in range(len(graph)):
            outdegree[i]=len(graph[i])
            
        indegree=[[] for i in range(len(graph))]
        
        # calculating the indegree of all the nodes which is a list of the indegree nodes
        for i in range(len(graph)):
            
            for val in graph[i]:
                indegree[val].append(i)
                
        queue=deque([])
        # starting with the nodes which doesnot have any outward nodes which are safe 
        for i in range(len(outdegree)-1,-1,-1):
            
            if outdegree[i]==0:
                queue.append(i)
        
        # we start with the outdegree nodes which are having no outward nodes and then try to remove the edges of the nodes which are linked to them in the next iteration.
        while len(queue)>0:
            index=queue.popleft()
            result.append(index)
            
            for val in indegree[index]:
                outdegree[val]=outdegree[val]-1
                
                if outdegree[val]==0:
                    queue.append(val)
        
        result=sorted(result)
        return result
                