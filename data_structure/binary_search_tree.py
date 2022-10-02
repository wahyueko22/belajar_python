from hashlib import new
from turtle import left


class Node:
    #constructor
    def __init__(self, parent, right, left, value):
        # instance variable
        self.parent = parent
        self.right = right
        self.left = left
        self.value = value

    def myfunc(self):
        print("Hello my name is " + self.name)
        
class BinarySearchTree:
    def __init__(self):
        print("start")
        self.first = None
        self.last = None
        self.root_node = None
    def add(self, value):
        if self.root_node == None:
            new_node = Node(None, None, None, value)
            self.root_node = new_node
        else:
            current_node = self.root_node
            while(current_node):
                if current_node.value >= value:
                    if current_node.right == None:
                        new_right_node = Node(current_node, None, None, value)
                        current_node.right = new_right_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    if current_node.left == None:
                        new_left_node = Node(current_node, None, None, value)
                        current_node.left = new_left_node
                        break
                    else:
                        current_node = current_node.left
    def searchValue(self, value):
        current_node = self.root_node
        found = False
        counter=0
        while(current_node):
            counter += 1
            print(counter)
            if current_node.value == value:
                found = True
                break
            elif current_node.value > value:
                current_node = current_node.right
            else :
                current_node = current_node.left
                
        if found:
            print("found")
        else:
            print("Not found")
        
    def printNode():
        current_node = self.root_node
        print(current_node.value) 
            
                   
           
                

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(9)
    bst.add(12)
    bst.add(13)
    bst.add(8)
    bst.add(7)
    bst.add(14)
     
    bst.searchValue(7)
    
        