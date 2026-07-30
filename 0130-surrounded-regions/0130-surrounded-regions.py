class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        # 1. Marker Initialization: F
        # Track cells that are part of the 'safe' dilated reconstruction
        reconstructed = [[0] * cols for _ in range(rows)]
        frontier = []
        
        # Populate the initial marker elements from the board boundaries
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    reconstructed[r][c] = 1
                    frontier.append((r, c))
                    
        # 2. Fixed-Point Iteration (Conditional Dilation): \delta_G^\infty(F)
        # Dilate the frontier using a 4-neighbor cross structuring element,
        # masking it strictly to cells where board[r][c] == 'O'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while frontier:
            next_frontier = []
            for r, c in frontier:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check boundary constraints and mask matching condition (G)
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 'O' and reconstructed[nr][nc] == 0:
                            reconstructed[nr][nc] = 1  # Element absorbs the dilation
                            next_frontier.append((nr, nc))
            
            frontier = next_frontier  # Move to the next wave of propagation

        # 3. Erosion Phase
        # Any 'O' cell not reached by the infinitary dilation is eroded into an 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and reconstructed[r][c] == 0:
                    board[r][c] = 'X'        