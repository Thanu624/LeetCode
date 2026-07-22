class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        red = defaultdict(list)
        blue = defaultdict(list)

        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)

        ans = [-1] * n
        q = deque([(0, 0), (0, 1)])  # 0=red, 1=blue
        vis = set()
        dist = 0

        while q:
            for _ in range(len(q)):
                node, color = q.popleft()

                if (node, color) in vis:
                    continue
                vis.add((node, color))

                if ans[node] == -1:
                    ans[node] = dist

                if color == 0:
                    for nxt in blue[node]:
                        q.append((nxt, 1))
                else:
                    for nxt in red[node]:
                        q.append((nxt, 0))
            dist += 1

        return ans
        