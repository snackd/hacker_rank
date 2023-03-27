class Solution:

    def minCost(self, startPos: List[int], homePos: List[int],
                rowCosts: List[int], colCosts: List[int]) -> int:

        startX, staryY = startPos
        homeX, homeY = homePos
        cost = 0

        while startX != homeX:
            if startX > home:
                startX -= 1
            else:
                startX += 1
            cost += rowCosts[startX]

        while startY != homeY:
            if startY > homeY:
                startY -= 1
            else:
                startY += 1

            cost += colCost[startY]
        return cost
