class Solution(object):
    @classmethod
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            end = x % 10
            start = x // div

            if start != end:
                return False

            x = (x % div) // 10
            div = div / 100

        return True

