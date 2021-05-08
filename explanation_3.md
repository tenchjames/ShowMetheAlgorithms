

for this problem i used a Node structure to hold the frequencies and characters
and used the fact that the character would be None for internal nodes. To keep 
the running time to O(n log n) i implemented a PriorityQueue class that used
pythons built in heapq. The built in implementation was a min queue so this
worked well with needing to pop the two lowest weighted items.

i did try to really think about some edge cases like if someone tried to encode
and empty string or the None type or a single character. to handle both of those cases and keep my 
algorithm consistent I added a "dummy" node as an internal node and added
a default value to the dummy node for that single character as a default.
I chose to make the None type return and empty string as well.

overall the running time is O (n log n) where n = the number of characters to
encode. For encoding to get the frequencies we loop over all n characters and
build the dictionary. we then loop over x frequencies to insert them into the
queue. we know x is <= n so at the worse case x == n and each insertion into 
a priority queue can be done in log n time. The next step of removing 2 items
from the queue and adding one back is still n iterations. Decoding the tree
requires looping over n characters and traversting the tree height which is
log n. so overall this operation is O(n log n).  Finally get_encodings
function traverses the height of the tree that was built. The huffman tree is
is mostly balanced because each iteration expands both the left and the right 
side of the tree. this height is log n. Overall none of these operations are 
nested so we are bounted by n log n * some constant. so this why O(n log n)
