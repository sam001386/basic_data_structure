## Union Find/disjoint set
## Detect cycle in an undirected graph
## Non optimization version
vertices = 6

def find_root(x, parent):
    x_root = x
    while parent[x_root] != -1:
        x_root = parent[x_root]
    return x_root

# 1 -- union successful, 0 -- union unsuccessful        
def union_vertices(x, y):
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)
    if x_root == y_root:
        return 0
    else:
        # y_root is the root of x_root
        parent[x_root] = y_root
        return 1

parent = [-1 for _ in range(vertices)]
edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [2, 5]]
for i in range(len(edges)):
    x = edges[i][0]
    y = edges[i][1]
    if union_vertices(x, y) == 0:
        print("cycle detected")
        break
    if i == len(edges) - 1:
        print("non cycle")
print(parent)
