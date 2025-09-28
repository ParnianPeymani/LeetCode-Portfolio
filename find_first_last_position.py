class Solution:
    def searchRange(self, nums, target):
        A = [i for i, num in enumerate(nums) if num == target]
        return [A[0], A[-1]] if A else [-1, -1]