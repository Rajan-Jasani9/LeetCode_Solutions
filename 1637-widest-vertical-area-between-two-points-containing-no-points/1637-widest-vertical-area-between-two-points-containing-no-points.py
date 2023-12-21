class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: (x[0],x[1]) )
        area = 0
        for i in range(1,len(points)):
            area = max(area, points[i][0] - points[i-1][0])
        return area