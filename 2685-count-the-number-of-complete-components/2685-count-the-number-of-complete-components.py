class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g ={v:{v} for v in range(n)}
        for u,v in edges:
            g[v].add(u);g[u].add(v)
        z=Counter(map(frozenset,g.values()))
        return sum(len(q)==f for q,f in z.items())
