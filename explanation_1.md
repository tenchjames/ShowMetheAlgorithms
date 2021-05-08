
I decided to use a doubly linked list to hold hold a queue of items
so i can remove the least recently used item once the queue is at capacity
I used a doubly linked list to make deletion easier. I need access to the 
previous node to move pointers during a delete operation. The other data
structure I used was a dictionary. The combination of these two data structures
allowed me to do all of the operations in constant time. set uses a python 
dictionary which can find a key in constant time. The delete operation is 
also constant time because the node has access to previous and next node
pointers so those swaps are constant. get is also constant because it uses
the hashmap/dictionary to do looksups.

