class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        oldColor = image[sr][sc]

        #if old color already == new color
        if oldColor == color:
            return image

        def dfs(r, c):
            #changing color of tile
            if image[r][c] == oldColor:
                image[r][c] = color

                #moving through grid
                if r >= 1:   #moving up
                    dfs(r-1, c)
                if r + 1 < R:    #moving down
                    dfs ( r + 1, c)
                if c >= 1:    #moving left
                    dfs(r, c - 1)
                if c + 1 < C:    #moving right
                    dfs(r, c + 1)
        
        dfs(sr, sc)
        return image
