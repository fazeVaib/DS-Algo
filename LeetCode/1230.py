# Toss strange coins


class Solution(object):
    def probabilityOfHeads(self, A, target):
        dp = [1.0]  # dp[heads] = prob
        for p in A:
            dp.append(0)
            for i in range(len(dp) - 1, 0, -1):
                dp[i] *= (1 - p)
                dp[i] += p * dp[i-1]
            dp[0] *= 1-p
        #print dp
        return dp[target]
