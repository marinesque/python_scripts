"""

140. Word Break II
Hard
Topics
Companies
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []


Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

T: 2^N (two decisions to make choose or not) + N^2
S: 2^N * N + N^2
"""

from builtins import str
from typing import List


class Solution:

    @classmethod
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        visited = {}

        def dfs(string):
            if string in visited:
                return visited[string]

            if not string:
                return [""]

            local_result = []

            for word in wordDict:
                if string.startswith(word):
                    sub_words = dfs(string[len(word):])

                    for sub_word in sub_words:
                        local_result.append(word + (" " if sub_word else "") + sub_word)

            visited[string] = local_result

            return local_result

        return dfs(s)


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
result = Solution.wordBreak(str, wordDict)

for s in result:
    print(s)