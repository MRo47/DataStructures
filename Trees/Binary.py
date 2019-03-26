import numpy as np
import random

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        if self.value != None:
            if value < self.value:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right == None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def print_tree(self):
        if self.left != None:
            self.left.print_tree()
        print(self.value)
        if self.right != None:
            self.right.print_tree()

    def find_val(self,value):
        if value < self.value:
            if self.left != None:
                self.left.find_val(value)
            else:
                print('Not found')
        elif value > self.value:
            if self.right != None:
                self.right.find_val(value)
            else:
                print('Not found')
        else:
            print('found')

    def find_parent(self,value):
        if value == self.value:
            print('im root')
        else:
            if self.left != None:
                if value < self.left.value:
                    self.left.left.find_parent(value)
                elif value > self.right.value:
                    self.left.right.find_parent(value)
                else:
                    return self
            

    def remove_node(self,value):
        if value < self.value:
            if self.left != None:
                self.left.remove_node(value)
            else:
                print('Not found')
        elif value > self.value:
            if self.right != None:
                self.right.remove_node(value)
            else:
                print('Not found')
        else:
            self = None
            print('removed node')



tr_val = [i for i in range(0,100)]
random.shuffle(tr_val)
print(tr_val)

root = Node(50)
for val in tr_val:
    root.insert(val)

root.print_tree()
root.find_val(0)

root.remove_node(10)
root.print_tree()
