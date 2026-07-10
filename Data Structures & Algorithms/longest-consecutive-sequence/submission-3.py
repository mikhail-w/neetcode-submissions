class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        s_nums = set(nums)
        longest = 1

        for num in s_nums:
            if (num - 1) not in s_nums:
                count = 1
                while (num + count) in s_nums:
                    count += 1
                    longest = max(longest, count)

        return longest