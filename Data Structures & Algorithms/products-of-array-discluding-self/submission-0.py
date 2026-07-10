class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        running_left = 1
        for i in range(n):
            result[i] = running_left
            running_left *= nums[i]

        running_right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= running_right
            running_right *= nums[i]

        return result