class Solution(object):
    def defangIPaddr(self, address):
        res=address.replace(".","[.]")
        return res

address = input()
print(Solution().defangIPaddr(address))