"""

28

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

# Knuth-Morris-Pratt
class Solution:
    @classmethod
    def getLPS(self, needle: str) -> []:
        if needle == "": return False
        lps = [0] * len(needle)

        j, i = 0, 1
        while i < len(needle):
            print(f"i:{i} j:{j}")
            if needle[i] == needle[j]:
                print(f"    needle[i]:{needle[i]} and needle[j]:{needle[j]} are equal")
                print(f"        make lps[{i}]:(j + 1){j + 1}, i++:{i + 1}, j++:{j + 1}")
                lps[i] = j + 1
                j += 1
                i += 1
            else:
                print(f"    needle[i]:{needle[i]} and needle[j]:{needle[j]} are NOT equal")
                if j == 0:
                    print(f"        j:{j} == 0")
                    print(f"            make lps[{i}]:{0}, i++:{i + 1}")
                    lps[i] = 0
                    i += 1
                else:
                    print(f"        j:{j} != 0")
                    j = lps[j - 1]
                    print(f"            make j:{j}")
        print(f"LPS: {lps}")
        return lps

    @classmethod
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        p = self.getLPS(needle)
        if len(haystack) < len(needle):
            return -1

        while i < len(haystack):
            if haystack[i] == needle[j]:
                print(f"    haystack[i]:{haystack[i]} and needle[j]:{needle[j]} are equal")
                print(f"        make i++:[{i + 1}], j++:{j + 1}")
                i += 1
                j += 1
                if j == len(needle):
                    retur
            else:
                print(f"    haystack[i]:{haystack[i]} and needle[j]:{needle[j]} are NOT equal")
                if j > 0:
                    j = p[j - 1]
                    print(f"        make i:[{i}], j = p[j-1]:{j}")
                else:
                    print(f"        make i++:[{i + 1}], j:{j}")
                    i += 1

        if i == len(haystack):
            return -1


result = Solution.strStr("sadbutsad", "sad")
print(result)