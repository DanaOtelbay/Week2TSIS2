class Solution(object):
    def numIdenticalPairs(self, nums):
        f = {}
        ans = 0
        for x in nums:
            if not x in f:
                f[x]=0
            f[x]+=1
            
        for x in f:
            n=f[x]
            ans+=(n*(n-1)//2)
            
        return ans

nums = input()
print(Solution().numIdenticalPairs(nums))