"""
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    values = set()
    results = LinkedList()
    current_node = llist_1.head
    while current_node:
        if current_node.value not in values:
            results.append(current_node.value)
            values.add(current_node.value)
        current_node = current_node.next
    
    current_node = llist_2.head
    while current_node:
        if current_node.value not in values:
            results.append(current_node.value)
            values.add(current_node.value)
        current_node = current_node.next
    
    return results
    

def intersection(llist_1, llist_2):
    results = LinkedList()
    l1_values = set()
    values_added = set()

    current_node = llist_1.head
    while current_node:
        l1_values.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        if current_node.value in l1_values and current_node.value not in values_added:
            results.append(current_node.value)
            values_added.add(current_node.value)
        current_node = current_node.next

    return results


# Test case 1
print("Test 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# expect
#3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
#6 -> 4 -> 21 -> 

# Test case 2
print("Test 2")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# expect unique elements from each list in union, but interset is empty
# because no items are in common
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
#

# Test case 3
print("Test 3")

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = []
element_6 = [1, 3, 5, 7, 9, 11]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
# expect the union to be all elemnts of second list
# and interset to be blank
# 1 -> 3 -> 5 -> 7 -> 9 -> 11 -> 
#

# Test case 4
print("Test 4")

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = []
element_8 = []

for i in element_7:
    linked_list_7.append(i)

for i in element_8:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))
# expect both to be empty set

# Test case 5
print("Test 5")

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_9 = [0, 4, 8, 1, 2]
element_10 = []

for i in element_9:
    linked_list_9.append(i)

for i in element_10:
    linked_list_10.append(i)

print (union(linked_list_9,linked_list_10))
print (intersection(linked_list_9,linked_list_10))
# expect union to have first set and interect to be blank
# 0 -> 4 -> 8 -> 1 -> 2 -> 
# 





