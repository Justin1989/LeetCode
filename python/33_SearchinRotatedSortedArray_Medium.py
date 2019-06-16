import unittest

class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if target < nums[0] < nums[M]: 
                L = M+1
            elif target >= nums[0] > nums[M]: 
                H = M
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1
        
class Test(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_some_cases(self):
        self.assertEqual(self.s.search([4,5,6,7,0,1,2],0), 4)
        self.assertEqual(self.s.search([4,5,6,7,0,1,2],3), -1)
        self.assertEqual(self.s.search([1,3,5],3), 1)
        self.assertEqual(self.s.search([1],1), 0)
            
if __name__ == '__main__':
    unittest.main()