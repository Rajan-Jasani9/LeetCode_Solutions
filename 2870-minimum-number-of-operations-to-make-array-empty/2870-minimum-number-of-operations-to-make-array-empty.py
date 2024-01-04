class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap={}
        for item in nums:
            hashmap[item]=1+hashmap.get(item,0)
        ans=0
        for key in hashmap:
            if hashmap[key]==1:
                return -1
            else:
                q=hashmap[key]//3
                r=hashmap[key]%3
                if r==0:
                    ans+=q
                
                else:
                    ans+=q+1
        return ans