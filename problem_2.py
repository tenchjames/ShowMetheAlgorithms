
import os


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    queue = Queue()
    results = []
    queue.enqueue(path)

    while not queue.is_empty():
        p = queue.dequeue()
        
        if os.path.isdir(p):
            for item in os.listdir(p):
                queue.enqueue(p + "/" +item)
        elif os.path.isfile(p):
            if p.endswith(suffix):
                results.append(p)

    return results

def find_files_recursive(suffix, path):
    results = []
    return helper(suffix, path, results)

def helper(suffix, path, results):
    if os.path.isfile(path):
        if path.endswith(suffix):
            results.append(path)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            helper(suffix, path + "/" + item, results)
    return results


files = find_files("c", "./testdir")

for file in files:
    print(file)



print("Recursive call")
r_files = find_files_recursive("c", "./testdir")

for file in r_files:
    print(file)

print("done with recursion")




