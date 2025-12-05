class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for i in range(len(accounts)):
            current_sum = 0
            for j in range(len(accounts[i])):
                current_sum += accounts[i][j]
            if current_sum > richest:
                richest = current_sum
        return richest

ok = Solution()
print(ok.maximumWealth([[1,2,3],[3,2,1]]))
