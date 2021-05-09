For problem two it felt like a approach would be a recursive call
I choose to pass a results array down to each recursive call and
return that at the end of the procedure. my recursion stops when
it locates a file, othewise if it meets a directory it recurses

I also decided to try an iterative approach so I would not have the overhead 
of the frame stack. I used a queue to iterate and do so in a breadth first
manner.

Time complexity
O(C^n)
the running time calculation on this problem is difficult. I am going to say
that the running time is actually exponential. My reasoning is because our
input is a single character and a single directory. However that single
directory can have many subdirectories, and each of those can have many.

Space complexity
O(C^n)
for both my recursive and my iterative solution the space complexity is still
the same. the queue based solutin in the worst case can store every possible
path. And the number of paths is exponential based on the input.
Then same is true for the recursive call. The difference is the space is
occupied 
by stack frames for each recursive call



