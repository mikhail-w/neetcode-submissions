from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        freq_arr = []
        for value, freq in freq.items():
            freq_arr.append((freq,value))

        sorted_arr = sorted(freq_arr, reverse=True)
        print(sorted_arr)
        res = []
        for i in range(k):
            res.append(sorted_arr[i][1])

        return res
