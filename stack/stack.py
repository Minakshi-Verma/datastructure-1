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

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = linkedList

    def __len__(self):
        # length=0
        # if self.head ==None and self.tail ==None:
        #     return length ==0
        # elif self.head != None snd self.tail != None:
        #     return length +=

 
        

    def push(self, value):
        return self.storage.add_to_tail(value) 

    def pop(self):
        if self.head != None and self.tail !=None:
            return self.storage.remove_tail()
        elif self.head ==None and self.tail ==None:
            return None
