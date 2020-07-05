#DFS
#Time comp  -->o(V+E)
#space comp -->o(V)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites)==0:
            return True
            
        adjList=dict()
        # creating a adjacency List for all the given vertices
        for val in prerequisites:
            cur_sub=val[0]
            pre_sub=val[1]
            
            if pre_sub not in adjList:
                adjList[pre_sub]=[cur_sub]
            else:
                adjList[pre_sub].append(cur_sub)
            if cur_sub not in adjList:
                adjList[cur_sub]=[]
          
    
        # print(adjList)
        # visited to store the nodes visited 
        visited=set()
        # to check if there is a repeated node in the given path
        rec_stack=set()
        
        # in case of unconnected components to know for existence of cycle or not we traverse for all the nodes
        for i in range(numCourses):
            if i not in visited:
                
                # If there is a cycle in the graph then we cannt have topological sort in that graph which means that all the courses cannot be done because of cycle detection in graph.
                if self.detect_cycle(adjList,i,visited,rec_stack):
                    return False
                
        return True
    
    
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
        return False
        
        
#BFS
#Time comp --> o(n)
#space comp--> o(n)
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        
        adjList=dict()
        
        for val in prerequisites:
            curr_course=val[0]
            pre_course=val[1]
            
            if pre_course not in adjList:
                adjList[pre_course]=[curr_course]
            else:
                adjList[pre_course].append(curr_course)
                
        indegree=[0 for i in range(numCourses)]
        
        for val in prerequisites:
            indegree[val[0]]+=1
            
        queue=deque([])
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        
        while len(queue)>0:
            course=queue.popleft()
            for val in adjList.get(course,[]):
                indegree[val]=indegree[val]-1
                
                if indegree[val]==0:
                    queue.append(val)
                    
        for val in indegree:
            if val>0:
                return False
            
        return True
            
        
        