import random
class Node:
    def __init__(self,assign_value):
        self.value_field=assign_value
        self.left_hand=None
        self.right_hand=None

class Tree:
    def __init__(self):
        self.tree_name='MammooTree'
        self.root_address=None

    def add_child(self,value):
        self.node = Node(value)
        if self.root_address!=None:
            self.add_node(self.root_address,self.node)
        else:
            self.root_address=self.node

    def add_node(self,node_address,node):
        if node.value_field > node_address.value_field and node_address.right_hand == None:
            node_address.right_hand = node
        elif node.value_field < node_address.value_field and node_address.left_hand == None:
            node_address.left_hand = node
        elif node.value_field < node_address.value_field and node_address.left_hand != None:
            self.add_node(node_address.left_hand, node)
        elif node.value_field > node_address.value_field and node_address.right_hand != None:
            self.add_node(node_address.right_hand, node)
        elif node.value_filed == node_address.value_field:
            print 'Value already found in tree'

    def print_btree(self):
        if self.root_address==None:
            print("Empty Tree")
        else:
            self.display_node(self.root_address)

    def display_node(self,node):
        print node.value_field
        if node.left_hand != None:
            self.display_node(node.left_hand)
        else:
            pass
        if node.right_hand != None:
            self.display_node(node.right_hand)

    def search_child(self,value):
        self.find_child(self.root_address,value)

    def find_child(self,node,value):
        if node.value_field < value and node.right_hand != None:
            self.find_child(node.right_hand,value)
        elif node.value_field > value and node.left_hand != None:
            self.find_child(node.left_hand,value)
        elif node.value_field == value:
            print 'Value found'
        elif node.value_field < value and node.right_hand == None:
            print 'Value not found'
        elif node.value_field > value and node.left_hand == None:
            print 'Value not found'

'''
NewTree=Tree()
NewTree.print_btree()
NewTree.add_child(10)
NewTree.add_child(11)
NewTree.add_child(12)
NewTree.add_child(9)
NewTree.add_child(8)
NewTree.add_child(7)
NewTree.print_btree()
NewTree.search_child(10)
NewTree.search_child(12)
NewTree.search_child(11)
NewTree.search_child(2)
'''

NewTree=Tree()
NewTree.print_btree()
elements = random.sample(range(1,100),50)
for i in elements:
    NewTree.add_child(i)
NewTree.print_btree()
NewTree.search_child(2)
NewTree.search_child(11)
