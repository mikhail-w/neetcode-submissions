class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                total = s_nums[i] + s_nums[left] + s_nums[right]
                if total == 0:
                    result.append([s_nums[i],s_nums[left], s_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and s_nums[left] == s_nums[left - 1]:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result

