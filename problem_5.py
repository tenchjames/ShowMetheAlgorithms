"""
Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

We can break the blockchain down into three main parts.

First is the information hash:
"""


import hashlib
from datetime import datetime


"""
We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:

"""

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(timestamp, data, previous_hash)
      self.next = None
      self.previous = None

    def calc_hash(self, timestamp, data, previous_hash):
        sha = hashlib.sha256()
        ts = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")
        hash_str = '{}{}{}'.format(data, previous_hash, ts).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
"""
Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!
"""

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.map = {}

    def append(self, data):
        if data is None:
            return None
        if self.head is None:
            block = Block(datetime.now(), data, 0)
            self.head = block
            self.tail = self.head
            self.map[block.hash] = block
            return block

        
        previous_hash = self.tail.hash
        block = Block(datetime.now(), data, previous_hash)
        self.tail.next = block
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.map[block.hash] = block
        return block
    
    def find_slow(self, hash_code):
        if hash_code is None:
            return None
        current_node = self.head

        while current_node:
            if current_node.hash == hash_code:
                return current_node
            current_node = current_node.next
        return None

    def find(self, hash_code):
        if hash_code not in self.map:
            return None
        else:
            return self.map[hash_code]
        

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.data) + "(" + str(cur_head.previous_hash) + "/" + str(cur_head.hash) + ")"  + " -> "
            cur_head = cur_head.next
        return out_string

#Test 1
print("Test 1")
blockchain = Blockchain()
blockchain.append("Hello")
blockchain.append("World")
foo_block = blockchain.append("foo")
bar_block = blockchain.append("bar")

print(blockchain)
# expect 4 items with each having the previous hash value match the hash of the
# prior block

print("Test 2")
print(foo_block.hash)
found_foo = blockchain.find(foo_block.hash)
print(found_foo.hash)
# expect both prints to be equal

print("Test 2a")
print(foo_block.hash)
found_foo = blockchain.find_slow(foo_block.hash)
print(found_foo.hash)
# expect both prints to be equal

print("Test 3")
unknown_block = blockchain.find("0000")
print(unknown_block)
# expect None 


print("Test 3a")
unknown_block = blockchain.find_slow("0000")
print(unknown_block)
# expect None 

print("Test 4")
none_block = blockchain.append(None)
print(none_block)
# expect None 

print("Test 5")
none_block = blockchain.find(None)
print(none_block)
# expect None


