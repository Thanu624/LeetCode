from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        if image[sr][sc] == color:
            return image

        q = deque()
        q.append([sr, sc])

        
        image_copy = [row[:] for row in image]
        original_color = image_copy[sr][sc]


        image_copy[sr][sc] = color

    
        while q:
            i, j = q.popleft()

    
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dx, dy = i + x, j + y
                if (
                    0 <= dx < len(image) and
                    0 <= dy < len(image[0]) and
                    image_copy[dx][dy] == original_color
                ):
                    image_copy[dx][dy] = color
                    q.append([dx, dy])

        return image_copy