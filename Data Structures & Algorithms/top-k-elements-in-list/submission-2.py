class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, freq in count.items():
            arr[freq].append(n)
        
        for i in range(len(nums), 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res