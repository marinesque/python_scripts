"""

139. Word Break
Medium
Topics
Companies
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
import collections
from builtins import str
from typing import List


class Solution:
    @classmethod
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = collections.deque([s])

        visited = set()

        while queue:
            word = queue.popleft()
            print(f"word: {word}")
            if word in visited:
                continue

            else:
                if not word:
                    return True

                visited.add(word)

                for start_word in wordDict:
                    print(f"start_word: {start_word}")
                    if word.startswith(start_word):
                        print(f"word[len(start_word):]: {word[len(start_word):]}")
                        queue.append(word[len(start_word):])

        return False

str = 'leetcode'
wordDict = ['cod', 'leet', 'le', 'et', 'e']
print(Solution.wordBreak(str, wordDict))

queue = collections.deque([str])
print(queue)