class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for indx in range(0, len(nums) -1):
            if (nums[indx] == nums[indx+1]):
                return True
            return False