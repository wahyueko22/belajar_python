
class Node:
    #constructor
    def __init__(self, prev, next, value):
        # instance variable
        self.prev = prev
        self.next = next
        self.value = value

    def myfunc(self):
        print("Hello my name is " + self.name)


class LinkedListNode:
    def __init__(self):
        print("start")
        self.first = None
        self.last = None
        self.node = None
    
    def add(self, value):
        if self.node == None:
            self.node = Node(self.last, None, value)
            self.last =  self.node
        else:
            newNode = Node(self.last, None, value)
            currentNode =  self.last
            currentNode.next = newNode
            self.last = newNode
            
    def add_recursive(self, node_param,  value):
        if node_param == None:
            node_param = Node(self.last, None, value)
            self.last = node_param
        else:
            if node_param.next:
                self.add_recursive(node_param.next, value)
            else:
                node_param.next = Node(self.last, None, value)
                self.last =  node_param.next
        
    def containValue(self, value):
        currentNode = self.node
        if currentNode.value == value :
            return "found"
        while (currentNode.next):
            currentNode = currentNode.next
            if currentNode.value == value :
                return "found"
        return "not found"
    
    def getLast(self):
        return self.last.value
    
    def printLinkedList(self):
        while(self.node != None):
            print(self.node.value)
            self.node = self.node.next
    
    def printFromTail(self):
        lastNode  = self.last
        while(lastNode):
            print(lastNode.value)
            lastNode = lastNode.prev 


if __name__ == "__main__":
    obj = LinkedListNode()
    obj.add(7)
    obj.add(5)
    obj.add(6)
    obj.add(4)
    print(obj.containValue(5))
    obj.printFromTail()
    #recursive
    obj_one = LinkedListNode()
    obj_one.add_recursive(obj_one.node, 4)
    obj_one.add_recursive(obj_one.node, 5)
    obj_one.printFromTail()