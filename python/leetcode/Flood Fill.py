class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image
        self.fill(image, sr, sc, len(image), len(image[0]), old_color, color)
        return image

    def fill(self, image, sr, sc, row, col, old_color, color):
        if sr == row or sr < 0 or sc < 0 or sc == col:
            return
        if image[sr][sc] is not old_color:
            return

        image[sr][sc] = color
        # right
        self.fill(image, sr + 1, sc, row, col, old_color, color)
        # left
        self.fill(image, sr - 1, sc, row, col, old_color, color)
        # top
        self.fill(image, sr, sc + 1, row, col, old_color, color)
        # bot
        self.fill(image, sr, sc - 1, row, col, old_color, color)

        return
