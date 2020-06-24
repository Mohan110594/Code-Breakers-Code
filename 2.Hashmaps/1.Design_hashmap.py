class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Time comp --> o(capacity)
        # space comp --> o(capacity)
        self.bucketlist=[None for i in range(10000)]
    
    def bucketindex(self,key):
        # Time comp --> o(1)
        # space comp -->o(1)
        return key%len(self.bucketlist)

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        # Time comp -->o(n)
        # space comp --> o(1)
        index=self.bucketindex(key)
        if self.bucketlist[index]==None:
            dummy=Node(-1,-1)
            dummy.next=Node(key,value)
            self.bucketlist[index]=dummy
        else:
            curr=self.bucketlist[index]
            while curr.next!=None:
                if curr.next.key==key:
                    curr.next.val=value
                    return
                curr=curr.next
            curr.next=Node(key,value)
                
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        # Time comp --> o(1)
        # space comp --> o(1)
        index=self.bucketindex(key)
        if self.bucketlist[index]==None:
            return -1
        curr=self.bucketlist[index]
        while curr!=None:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        # Time comp --> o(n)
        # space comp --> o(1)
        index=self.bucketindex(key)
        prev=self.bucketlist[index]
        if prev==None:
            return -1
        curr=prev.next
        while curr!=None:
            if curr.key==key:
                prev.next=prev.next.next
                curr.next=None
                return
            prev=curr
            curr=curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)