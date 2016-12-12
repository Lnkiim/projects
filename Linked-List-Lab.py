
# coding: utf-8

# ## Linked List Lab
# 
# A linked list is a data structre frequently used in computer science and is part of a standard set of interview questions. 
# 
# Other common data structred are hash tables and trees which we will cover later in the course.
# 
# ![](assets/linked_list.png)
# 
# * A linked list starts with an entry point which is called a node. 
# * Each node has two attributes namely a value and a pointer to another node. 
# * In this lab we will create two classes. A class Node and a class Linked List to wrap the linked nodes.
# 
# 1. Create a class for Linked List that initializes a linked list and returns a pointer to the head of the linked list. 
# 2. Create a function (inside Linked List) that appends an element to the end of the linked list
# 3. Create a function that pops an element from the end of the list
# 4. Use \__repr\__ to print out the elements of the linked list
# 5. Create a function that adds an element to the beginning of the list
# 6. Create a function that delets the first element from the linked list
# 
# 
# **Bonus:**
# 
# Create a circular linked list allowing you to access the linked list from the beginning and the end. Implement the functions above for the circular list. How can you increase the efficiency of the algorithm for inserting and deleting?

# LINKED LIST ( OSM)
# - Attributes: head, tail
# - make a new node --> call init node function
# -  when a new node is created, it needs to change the .next attribute's value
# - 
# 
# 
# NODE(online store)
# - does it need any methods?
# 
# 
# 
# 
# 
# 

# In[3]:

class Node:
    def __init__(self, value):
        self.value= value
        self.next = None
    
class LL:
    def __init__(self, head= None, tail= None):
        self.head = head
        self.tail = tail
        return self.head 
    
    def __repr__(self):
        prints = ""
        if self.head != None:
            while 
            pointer = self.head
            prints += pointer.value + " "
            
            
        return '(x=%s, y=%s)' % (self.x, self.y)
    
    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def pop(self):
        if self.head == self.tail:
            holder = self.head
            self.head = None
            self.tail = None
            return holder
        else:
            previous = self.head 
            while previous.next != self.tail:
                previous = previous.next 
            self.tail = previous
            holder = previous.next
            previous.next = None
            return holder
        
        #what about special case where LL only has one node? pop should still work
        
        
    
    
    


# In[ ]:




# In[ ]:



