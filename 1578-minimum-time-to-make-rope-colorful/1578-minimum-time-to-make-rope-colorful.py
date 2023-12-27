class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l,r = 0,1
        cost = 0
        while r <= len(colors)-1:
            if colors[l] == colors[r]:
                r+=1
            else:
                if l < r+1:
                    cost += sum(neededTime[l:r]) - max(neededTime[l:r])
                l = r
                r+=1
        
        cost += sum(neededTime[l:r]) - max(neededTime[l:r])
        return cost