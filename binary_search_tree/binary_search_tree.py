"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
     
        #if node is instantiated with None or node has no value
        if self.value is None:
            #set self.value to the value of inserted node
            self.value = value
        # if node already has a value(self.value) and inserted value >= existing node value
        elif value >= self.value:
            # if new value is greater...it will go on right, check if we already have a node on right
            if self.right:
            # if node.right is there, insert the value
                self.right.insert(value)            
            # if there is no right node, insert the new node with the value
            else:
                self.right = BSTNode(value)
        #Now if the value< self.value, we insert the new value on left(check using ifel or just move to else block)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)  
    #-------------------------------------     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value ==target:
            return True

        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)

        elif self.value< target:
            if self.right is not None:
                return self.right.contains(target)
        else:
            return False
    #----------------------------------------

    # Return the maximum value found in the tree
    def get_max(self):
        # #recurse right until none
        # if self.left is None and self.right is None:
        #     Max = self.value
        #     return Max
        # elif self.right is None:
        #     Max = self.value
        #     return Max
        # else:
        #     self.get_max()
        #     return Max
        #------------
       
        
        if self.right ==None:
            return self.value
        else:
            return self.right.get_max()      
    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # base = self.value
        # recursively apply the function to base node, left nodes and right nodes
        if not self.left and not self.right:
            return fn(self.value)
        elif self.left and not self.right:
            return fn(self.value), self.left.for_each(fn)
        elif self.right and not self.left:
            return fn(self.value), self.right.for_each(fn)
        elif self.left and self.right:
            return fn(self.value), self.left.for_each(fn), self.right.for_each(fn)
# values =[]
# bst =BSTNode(2)
# bst.insert(3)
# bst.insert(7)
# bst.insert(8)
# bst.insert(90)
# cb = Lambda x: values.append(x)
# bst.for_each(Lambda x:values.append(x))
# print(values)    


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
