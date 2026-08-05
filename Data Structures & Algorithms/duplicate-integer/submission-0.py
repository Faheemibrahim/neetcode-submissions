class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counter = 0
        set1 = set()

        for num in nums:
            set1.add(num)

        set_size = len(set1)
        list_size = len(nums)

        if set_size < list_size:
            return True
        else:
            return False

            