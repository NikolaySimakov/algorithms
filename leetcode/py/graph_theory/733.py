from typing import List


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        n = len(image[0])
        m = len(image)

        c = image[sr][sc]
        image[sr][sc] = color

        for i, j in [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]:
            if 0 <= i < m and 0 <= j < n:
                if image[i][j] == c:
                    image = self.floodFill(image, i, j, color)

        return image


s = Solution()
g = [[0, 0, 0], [0, 0, 0]]
print(s.floodFill(g, 0, 0, 0))
