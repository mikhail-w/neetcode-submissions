class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx,num in enumerate(nums):
            comp = target - num
            if comp in dic:
                sl = sorted([idx,dic[comp]])
                return [sl[0],sl[1]]
            dic[num] = idx