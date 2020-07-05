#DFS
Time comp --> o(n)
space comp --> o(n)
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def __init__(self):
        self.res=0
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        if len(employees)==0:
            return 0            
        res=0
        e_dict=dict()
        for emp in employees:
            e_dict[emp.id]=emp
        
        self.dfs(e_dict,id)
        
        return self.res
        
        
    def dfs(self,e_dict,id):
        
        self.res=self.res+e_dict[id].importance
            
        for j in e_dict[id].subordinates:
            self.dfs(e_dict,j)
            
        
        
#BFS
Time comp --> o(n)
space comp --> o(n)

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id  
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        if len(employees)==0:
            return 0            
        emp_dict=dict()
        for emp in employees:
            emp_dict[emp.id]=emp
            
        queue=deque([id])
        
        result=0
        
        while len(queue)>0:
            index=queue.popleft()
            
            result=result+emp_dict[index].importance
            
            for employee in emp_dict[index].subordinates:
                    queue.append(employee)
                
        return result
            