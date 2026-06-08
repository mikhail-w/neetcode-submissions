class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        arr = ((freq,num) for num,freq in freq_dict.items())
        s_arr = sorted(arr,reverse=True, key=lambda x:x[0])
        res = []
        for i in range(k):
            res.append(s_arr[i][1])
        return res


        