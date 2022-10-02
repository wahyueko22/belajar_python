import collections

#https://algodaily.com/lessons/dfs-vs-bfs/python
class Tree_Node:
    def __init__(self, root_value, children_nodes):
        self.value = root_value
        self.children_nodes = children_nodes


def breadth_first_search(Root_Node):
    queue = collections.deque()
    queue.append(Root_Node.value)

    while queue:
        node_value = queue.popleft()
        print(node_value)
        children_nodes = nodes_dic[node_value]

        for i in children_nodes:
            if i == None:
                continue
            queue.append(i)
            
# test code

nodes_dic =  {"A":["B","C"],
              "B":["D","E"],
              "C":["F","G"],
              "D":[None],
              "E":["H","I"],
              "F":[None],
              "G":["J", None],
              "H":[None],
              "I":[None],
              "J":[None]}

root_node_value = next(iter(nodes_dic.keys()))
print("root_node_value : ", root_node_value)
root_node_children = next(iter(nodes_dic.values()))
print("root_node_children : ", root_node_children)
root_node = Tree_Node(root_node_value ,root_node_children )

breadth_first_search(root_node)