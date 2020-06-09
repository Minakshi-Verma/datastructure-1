"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList
from singly_linked_list import Node

# Stack Class with array data type

class Stack_arr:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # if len(self.storage) >0:
        return self.size
        

    def push(self, value):
        self.storage.append(value) 
        self.size += 1

    def pop(self):
        # if not self.size:        
        if self.size < 1:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

#Stack class with linkedlist data type
class Stack:
    def __init__(self):
        self.size = None
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):       
        self.storage.add_to_tail(value)
        self.size += 1
        print(type(self.size))
    
    def pop(self):
        #if no head node in the linkedlist
        if self.size ==0:
            print("stack is empty")
            return None            
        else:   
            self.size -=1
            return self.storage.remove_tail()         
         
            
