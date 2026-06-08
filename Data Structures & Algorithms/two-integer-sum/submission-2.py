class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,num in enumerate(nums):
            comp = target - num
            if comp in seen:
                sl = sorted( [idx,seen[comp]])
                return [sl[0],sl[1]]
            seen[num] = idx
