class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num) - 1] *= -1
        res = []
        for num in nums:
            if nums[abs(num) -1] > 0:
                res.append(abs(num))
                nums[abs(num) - 1] *= -1
        return res