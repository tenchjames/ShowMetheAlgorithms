For this problem recursion was a good approach to solving this problem. The
base case is when the user is found the algoiritm will return true. 
Thinking about this problem I considered what would happen if a subgroup added
some other group higher up in the directory as a member. I would end up in 
and infinite recursive call. So I added a set data structure to check if 
we already explored a group, if so I don't recurse over it again.

Time complexity O(C^n)
Overall the worst case running time for this problem is also exponential. 
Looking with our input being a single user and a single group the problem grows 
based on the number of sub groups in each group, and each of those sub groups
can have many subgroups. In the worse case if we do not find the user we will 
iterate over all users in the tree under the initial group, and all of the 
subgroups in the subtree. 

Space complexity O(C^n)
For the same reasons the time complexity is exponential relative to the two 
inputs so is the space complexity. The storage space being used is based on 
the recursive calls each needing to go onto the stack. Each of these frames 
will take up memory
