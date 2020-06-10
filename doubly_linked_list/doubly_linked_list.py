"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    # def get_next(self):
    #     return self.next

    # def get_value(self):
    #     return self.value   


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #new_node will become head
        #new_node(prev) will point to None
        #new_node(next)will point to next node
        #first or old node(next) will point to the "value" of newly added node        
        #New or last added node(prev) will point to the "value" of previous node value
        #new node(next) will point to None
        new_node = ListNode(value)
        #check if doublylinked list is empty or have nodes
        # if self.head ==None and self.tail ==None:
        if not self.head and not self.tail:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next = self.head
            self.head.prev= new_node 
            self.head = new_node       

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # if double linked list is empty
        if not self.head:            
            return None
        # if double linked list has only one node, get the value
        if not self.head.next:
            current_head = self.head
            return current_head.value
        #if there are more than 1 nodes, redirect the head to 2nd node
        else:            
            self.head.next = self.head
            self.head.prev = None
                       

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        #check if doublylinked list is empty or have nodes
        # if self.head ==None and self.tail ==None:
        if not self.head and not self.tail:
            self.head=new_node
            self.tail=new_node
            self.length +=1
        else:
            # new_node.prev = self.tail
            # self.tail.next=new_node
            # self.tail = new_node
            self.tail.insert_after(value)
            self.tail= self.tail.next
            self.length +=1
          

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #if linked list is empty
        if not self.tail:
            return None
            # if double linked list has only one node, get the value
        if not self.tail.prev:
            current_tail = self.tail
            return current_tail.value
        #if there are more than 1 nodes, redirect the tail to previous node
        else:
            self.tail.prev = self.tail
            self.tail.next = None       
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #Delete the existing node
        node.delete()
        #Insert the node as head node
        self.head.insert_before(node)
        self.head=node        
        node.prev= None

       

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # Delete  the  existing node
        node.delete() 
        #Add the node as a tail node
        self.tail.insert_after(node)
        self.tail= node
        node.next = None
        

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #if node was the head
        if not self.head and not self.tail:
            self.head = None
            self.tail= None                 
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
            self.length -=1          
        if self.tail is node :
            self.tail= self.tail.prev
            self.tail.next=None
            self.length -=1 
        else:
            node.delete()
            self.length -=1        
       
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # while self.head != None:
        #     if self.head.value>self.head.next.value:
       Pass
                 
                 

            


        
