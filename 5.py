class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        pro=1
        ns=str(n)
        for x in ns:
            sum+=int(x)
            pro*=int(x)
        return abs(pro-sum)

n = input()
print(Solution().subtractProductAndSum(n))