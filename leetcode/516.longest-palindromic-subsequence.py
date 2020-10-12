#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # Create a table to store results of subproblems
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Strings of length 1 are palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Build the table. Note that the lower diagonal values of table are
        # useless and not filled in the process. The values are filled in a
        # manner similar to Matrix Chain Multiplication DP solution (See
        # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
        # cl is length of substring
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j] and cl == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]);

        return dp[0][n - 1]

# @lc code=end

