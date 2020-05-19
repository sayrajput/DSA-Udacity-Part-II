class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.HashTable = dict()

        #dummy head and tail
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    

    def get(self, key):
        if self.capacity == 0:
            return -1
        
        if not bool(key) or key not in self.HashTable:
            return -1
        
        node = self.HashTable[key]
        self.move_to_front(node)
        return node.value
    
    def set(self,key,value):
        if self.capacity == 0:
            return -1
        
        if not bool(key):
            return -1
        
        if key in self.HashTable:
            node = self.HashTable[key]
            node.value = value
            self.move_to_front(node)
        else:
            node = Node(key,value)
            self.add(node)
            self.HashTable[key] = node
        
        if len(self.HashTable) > self.capacity:
            self.remove_lru()


    def move_to_front(self, node):
        if node == self.head.next:
            return
        
        self.remove(node)
        self.add(node)
    
    def remove(self,node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
    
    def remove_lru(self):
        node = self.tail.prev
        self.remove(node)
        del self.HashTable[node.key]

    def add(self,node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next  = node
    

    def clear(self):
        """Empties the cache."""
        self.HashTable.clear()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)




if __name__  == '__main__':
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)


    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    print(our_cache.set(6, 6))

    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(3))
