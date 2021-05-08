For problem two it felt like a approach would be a recursive call
I choose to pass a results array down to each recursive call and
return that at the end of the procedure. my recursion stops when
it locates a file, othewise if it meets a directory it recurses

I also decided to try an iterative approach so I would not have the overhead 
of the frame stack. I used a queue to iterate and do so in a breadth first
manner.

the running time calculation on this problem is difficult. I am going to say
that the running time is actually exponential. My reasoning is because our
input is a single character and a single directory. However that single
directory can have many subdirectories, and each of those can have many.

