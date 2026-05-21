class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for i in nums:
            if i in my_map:
                return True
            else:
                my_map[i] = 1
        return False
