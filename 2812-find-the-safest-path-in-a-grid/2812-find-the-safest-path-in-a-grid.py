class Solution:
    def bfs(self, score, grid) -> None:
        n = len(grid)
        q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    score[i][j] = 0
        
        while q:
            r, c = q.popleft()
            s = score[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and score[nr][nc] > s + 1:
                    score[nr][nc] = s + 1
                    q.append((nr, nc))

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        score = [[inf] * n for _ in range(n)]
        self.bfs(score, grid)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = set()
        heap = [(-score[0][0], 0, 0)]  

        while heap:
            safeScore, r, c = heapq.heappop(heap)
            safeScore *= -1  
            if r == n - 1 and c == n - 1:
                return safeScore
            if (r, c) in vis:
                continue
            vis.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in vis:
                    heapq.heappush(heap, (-min(score[nr][nc], safeScore), nr, nc))
        
        return -1