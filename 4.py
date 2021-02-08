class Solution(object):
    def largestAltitude(self, gain):
        max=0
        res=0
        for x in gain:
            res+=x
            if max<res:
                max=res
                
        return max

gain = input()
print(Solution().largestAltitude(gain))
