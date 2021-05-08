
This problem was very wide open. I think the focus was to understand hashing
a bit more while implementing a linked list like structure. I decided to
add pointers for a head and tail in the block chain. I did this because 
my understanding of the blockchain is that it will continue to grow so
insertion is now constant with access to the tail pointer. the running time for
the find method is n where n == the length of the blockchain as the worst case.

could we do better? we could add a hashmap that mapped the hash -> block and
this would allow for constant time lookups with find. 
However implementing this change also increases the storage for the blockchain
so that needs to be considered with a large structure. I did implement two 
versions to practice both. the find_slow will run in O(n) time but require less 
storage, where find will operate in O(1) time but require additional storage.
