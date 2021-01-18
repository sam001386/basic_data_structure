
# LC 1584

# Prim approach
class Solution(object):
    def minCostConnectPoints(self, A):
        seen = set()
        # 这里假设初始的节点是0
        seen.add(0)
        # 当前节点
        cur = 0
        res = 0
        pq = []
        while len(seen) < len(A):
            for nxt in range(len(A)):
                # 如果“下一个节点”已经被访问过了，或者等于当前节点则跳过
                if cur == nxt or nxt in seen:
                    continue
                # 这里使用heap（priority queue）来实现找到一条新的边
                else:
                    heapq.heappush(pq, (abs(A[cur][0] - A[nxt][0]) + abs(A[cur][1] - A[nxt][1]), nxt))
            # 如果当前节点已经被访问，则从heap（priority queue）弹出
            while pq[0][1] in seen:
                heapq.heappop(pq)
            res += pq[0][0]
            cur = pq[0][1]
            heapq.heappop(pq)
            # 记录下当前节点已经被访问过了
            seen.add(cur)

        return res

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
