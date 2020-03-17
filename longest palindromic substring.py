s = str(input())


class Solution(object):
    def palindrom(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        self.max_str = " "
        self.max_len = 0

        def is_palindrom(left, right):
            l, r = left, right
            while (l >= 0 and r < len(s) and s[i] == s[l]):
                l -= 1
                r += 1
            if l - r + 1 > self.max_len:
                self.max_len = l - r + 1
                self.max_str = s[l + 1: r]
        for i in range(len(s)):
            is_palindrom(i, i)
            is_palindrom(i, i + 1)
        return self.max_str


answer = Solution()
print(answer.palindrom(s))