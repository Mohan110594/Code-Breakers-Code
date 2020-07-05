#DFS
#Time comp ---> o(number of rooms+number of keys)
#space comp --> o(number of rooms)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited=set()
        
        self.dfs(rooms,visited,0)
        
        return len(visited)==len(rooms)
        
    def dfs(self,rooms,visited,index):
        
        if index in visited:
            return
        visited.add(index)
        
        for room in rooms[index]:
            self.dfs(rooms,visited,room)
        
        
        
        
#BFS

#Time comp ---> o(number of rooms+number of keys)
#space comp -->o(number of rooms)

from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms)==0:
            return True
        
        queue=deque([0])
        visited=set()
        
        while len(queue)>0:
            index=queue.popleft()
            if index in visited:
                continue
            else:
                visited.add(index)
            
            for room in rooms[index]:
                queue.append(room)
                
        return len(visited)==len(rooms)
        