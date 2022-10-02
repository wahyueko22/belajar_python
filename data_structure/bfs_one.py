# binary tree / graph : https://www.educative.io/answers/how-to-implement-a-breadth-first-search-in-python
# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
#       A
#   B       C
#D      E       F
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['E','F'],
  'D' : ['E', 'F'],
  'E' : ['F'],
  'F' : []
}

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print(s)
    for neighbour in graph[s]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)


if __name__=="__main__":
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue
    # Driver Code
    bfs(visited, graph, 'A')