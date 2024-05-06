"""

49. Group Anagrams
Medium
Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
from collections import defaultdict
from typing import List


class Solution:
    @classmethod
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            print(f"string: {s}")
            count = [0] * 26
            for c in s:
                print(f"current c: {c}")
                count[ord(c) - ord('a')] += 1 #unicode code
                print(f"count[{ord(c) - ord('a')}]: {count[ord(c) - ord('a')]}")

            key = tuple(count)
            print(f"key: {key}")
            anagram_dict[key].append(s)

        return anagram_dict.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(strs))
