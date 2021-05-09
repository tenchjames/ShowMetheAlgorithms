
for both operations i utilized the set data structure to determine if
a value belongs. I made this decision to keep the running time at 
O(n + m) where n = len(list1) and m = len(list2). without the sets 
the brute force approach would have had a loop within a loop 
checking if the item was already found. so the sets improve the time 
complexity. 


Space complexity

union creates a new linked list so in the worst case the items in
n and m could all be unique so the total space would be O(n + m)

intersect also creates a new linked list. In the worst case the 
two lists could be the exact same. In that case we would only store 
all the values from n in the l1_values set. while we would also store
m values in the values_added set. So the storage is also O(n + m) in
the worst case
