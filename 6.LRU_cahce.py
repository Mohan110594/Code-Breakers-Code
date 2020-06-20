#Double Linked List+HashMap to store the key value and their nodes
class  Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.cache=dict()
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def add_start(self,node):
        # Time --> o(1)
        # space --> o(1)
        node.prev=self.head
        node.next=self.head.next
        self.head.next=node
        node.next.prev=node
        
    def remove_node(self,node):
        # Time --> o(1)
        # space --> o(1)
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        # Time --> o(1)
        # space --> o(1)
        if key not in self.cache:
            return -1
        node1=self.cache[key]
        self.remove_node(node1)
        self.add_start(node1)
        return node1.val

    def put(self, key: int, value: int) -> None:
        # Time --> o(1)
        # space --> o(n)
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove_node(node)
            self.add_start(node)
        else:
            if len(self.cache)==self.capacity:
                tailnode=self.tail.prev
                del self.cache[tailnode.key]
                self.remove_node(tailnode)
            node1=Node(key,value)
            self.add_start(node1)
            self.cache[key]=node1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)