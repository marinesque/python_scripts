from builtins import str


class Solution:
    @classmethod
    def numDecodings(self, s: str) -> int:

        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        return dp[0]

        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            result = dfs(i + 1)
            if (i + 1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                result += dfs(i + 2)

            dp[i] = result
            return result

        return dfs(0)

    @classmethod
    def numDecodings2(self, s: str) -> int:

        res = 0
        if s[0] == "0":
            return res
        dp = [1]
        for i in range(1, len(s)):
            if s[i] == "0":
                dp.append(0)
            else:
                dp.append(dp[i - 1])
            print(dp)
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                if i > 1:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += dp[0]
            print(dp)
        print(dp)
        return dp[-1]

str = '121031'
print(Solution.numDecodings2(str))
print(Solution.numDecodings(str))

dp = {len(str): 1}
print(dp)