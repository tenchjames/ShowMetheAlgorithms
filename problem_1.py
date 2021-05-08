"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:

"""

# to maintain order of least recently accessed we will keep nodes
# in a linked list, using a double linked list so we can do deletion
# in constant time as required


class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


# to be able to delete a node in the middle
class DoublyLinkedQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        self.num_elements += 1;

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = node.next
        self.num_elements -= 1
        return node

    def remove(self, node):
        if self.is_empty():
            return
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            node.next.previous = None
        elif node == self.tail:
            self.tail = node.previous
            node.previous.next = None
        elif node.next is None and node.previous is None:
            # this node must have been deleted already
            return
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
        node.next = None
        node.previous = None
        self.num_elements -= 1

"""

dq = DoublyLinkedQueue()
dq.enqueue(DoubleNode(1))
dq.enqueue(DoubleNode(2))
n3 = DoubleNode(3)
dq.enqueue(n3)
dq.enqueue(DoubleNode(4))
print(dq.size())
# expect 4
n1 = dq.dequeue()
print(n1.value)
# expect 1
print(dq.size())
# expect 3
dq.remove(n3)
print(dq.size())
# expect 2
print(dq.head.value)
# expect 2
print(dq.tail.value)
# expect 4
dq.enqueue(n3)
print(dq.tail.value)
# expect 3
dq.remove(n3)
print(dq.tail.value)
# expect 4
dq.remove(n3)
dq.remove(n3)
dq.remove(n3)
"""


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.queue = DoublyLinkedQueue()
        self.map = {}
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        node = self.map.get(key)
        if node is None:
            return -1
        self.move_to_back_of_queue(node)
        return node.value

    def move_to_back_of_queue(self, node):
        self.queue.remove(node)
        self.queue.enqueue(node)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.map:
            node = DoubleNode(key, value)
            # if the node is not in the map we are trying to insert
            # so if the queue is already at capacity we need to remove the oldest
            # node from both the map and the queue
            if self.queue.size() == self.capacity:
                to_delete = self.queue.dequeue()
                self.map.pop(to_delete.key)
            self.queue.enqueue(node)
        else:
            node = self.map[key]
            # a set operation counts as access, so move existing item to the back of the queue
            node.value = value
            self.move_to_back_of_queue(node)
        self.map[key] = node


print("Test 1 from the assignment")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# see tests above on my doublely linked list too
print("Test 2")
one_item_cache = LRU_Cache(1)

one_item_cache.set(1, "A string")
one_item_cache.set(2, "Another string")
print(one_item_cache.get(1))
# expect -1 because cache should have removed 

print("Test 3")

big_cache = LRU_Cache(1000000)
for i in range(0, 1000000):
    big_cache.set(i, i)

print(big_cache.get(0))
# expect 0

big_cache.set(1000001, 1000001)
print(big_cache.get(1))
# expect -1

