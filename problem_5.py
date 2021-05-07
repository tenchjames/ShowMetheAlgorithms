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

    def append(self, data):
        if self.head is None:
            self.head = Block(datetime.now(), data, 0)
            self.tail = self.head
            return
        
        previous_hash = self.tail.hash
        block = Block(datetime.now(), data, previous_hash)
        self.tail.next = block
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.data) + "(" + str(cur_head.previous_hash) + "/" + str(cur_head.hash) + ")"  + " -> "
            cur_head = cur_head.next
        return out_string

#Test 1
blockchain = Blockchain()
blockchain.append("Hello")
blockchain.append("World")
blockchain.append("foo")
blockchain.append("bar")

print(blockchain)



