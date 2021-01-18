

# Kruskal approach
class Solution(object):
    def minCostConnectPoints(self, A):
        distance = []
        parents = [i for i in range(len(A))]
        res = 0

        def find(x):
            root = x
            while parents[root] != root:
                parents[root] = parents[parents[root]]
                root = parents[root]
            return root

        for i in range(len(A)):
            cur_dis = 0
            for j in range(i + 1, len(A)):
                heapq.heappush(distance, ((abs(A[i][0] - A[j][0]) + abs(A[i][1] - A[j][1])), i, j))

        for _ in range(len(distance)):
            dis, x, y = heapq.heappop(distance)
            if find(x) == find(y):
                continue 
            else:
                res += dis
                parents[find(x)] = find(y)  
        return res
