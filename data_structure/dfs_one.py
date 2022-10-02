#https://favtutor.com/blogs/depth-first-search-python#:~:text=Traversal%20means%20that%20visiting%20all,graph%20or%20tree%20data%20structure.
# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
             
def dfs_list(visited_list, graph, node):  #function for dfs with list
    if node not in visited_list:
        print (node)
        visited_list.append(node)
        for neighbour in graph[node]:
            dfs_list(visited_list, graph, neighbour)

if __name__ == "__main__":
    visited = set() # Set to keep track of visited nodes of graph.
    visited_list = [] # List to keep track of visited nodes.
    queue_list = [] 
    # Driver Code
    print("Following is the Depth-First Search")
    #dfs(visited, graph, '5')
    dfs_list(visited_list, graph, '5')