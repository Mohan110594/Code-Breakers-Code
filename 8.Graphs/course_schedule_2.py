#BFS
#Time comp --> o(V+E)
#space comp ---> o(V+E)

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjList=[[] for i in range(numCourses)]
        
        indegree=[0 for i in range(numCourses)]
        
        result=[]
        
        for course in prerequisites:
            indegree[course[0]]+=1
            adjList[course[1]].append(course[0])
            
        queue=deque()
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
                
                
        while len(queue)>0:
            index=queue.popleft()
             
            result.append(index)
            
            for nextcourse in adjList[index]:
                indegree[nextcourse]=indegree[nextcourse]-1
                
                if indegree[nextcourse]==0:
                    queue.append(nextcourse)
                    
        if len(result)== numCourses:
            return result
        return []
                
            
 #DFS       
 
 #Time comp --> o(V+E)
 #space comp --> o(V+E)
 class Solution:
    def __init__(self):
        self.result=[]
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
       
        adjList=dict()
        result=[]
        # creating a adjacency List for all the given vertices
        
        for i in range(numCourses):
            if i not in adjList:
                adjList[i]=[]
                
        for val in prerequisites:
            adjList[val[1]].append(val[0])

        # visited to store the nodes visited 
        visited=set() 
        # to check if there is a repeated node in the given path
        rec_stack=set()
        
        # in case of unconnected components to know for existence of cycle or not we traverse for all the nodes
        for i in range(numCourses):
            if i not in visited:
                
                # If there is a cycle in the graph then we cannt have topological sort in that graph which means that all the courses cannot be done because of cycle detection in graph.
                if self.detect_cycle(adjList,i,visited,rec_stack):
                    return []
        return self.result[::-1]
    
    
    def detect_cycle(self,adjList,course,visited,rec_stack):
        
        visited.add(course)
        
        rec_stack.add(course)
        
        # if the neighbouring courses are not in the adjacency list it means the course is not present so we return False indicating that course culdnot be done
        
        if course not in adjList:
            return False
        
        
        
        for course_nei in adjList[course]:
            
            # rec_stack has the current path for the given node and see the existence of cycle in the current path
            
            if course_nei in rec_stack:
                return True
            
            # if the course is not visited and there is  cycle in the  given prerequisites it means that all the courses cannt be done
            
            if course_nei not in visited and self.detect_cycle(adjList,course_nei,visited,rec_stack):
                return True
        
        # after the dfs for the current element we remove all the nodes encountered in the given path
        
        rec_stack.remove(course)
        self.result.append(course)
        return False
        
        
        
        
        