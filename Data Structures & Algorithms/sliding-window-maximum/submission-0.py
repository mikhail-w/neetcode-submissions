class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        output = []

        while right <= len(nums):
            temp = nums[left:right]
            output.append(max(temp))
            left += 1
            right += 1

        return output
        # //print(output)

