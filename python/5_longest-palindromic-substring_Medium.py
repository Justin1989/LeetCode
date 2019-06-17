import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAt(s, i, i)
            len2 = self.expandAt(s, i, i + 1)
            l = len1 if len1 > len2 else len2
            if l > end - start:
                start = i - (l-1)//2
                end = i + l//2 + 1
        return s[start: end]
        
    def expandAt(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
        
class Test(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_some_cases(self):
        self.assertEqual(self.s.expandAt('abcb',2,2), 3)
        self.assertEqual(self.s.expandAt('abcb',2,3), 0)
        self.assertEqual(self.s.expandAt('abbc',1,2), 2)
        
        self.assertEqual(self.s.longestPalindrome('abcb'), 'bcb')
        self.assertEqual(self.s.longestPalindrome('babad'), 'bab')
        self.assertEqual(self.s.longestPalindrome('cbbd'), 'bb')
            
if __name__ == '__main__':
    unittest.main()