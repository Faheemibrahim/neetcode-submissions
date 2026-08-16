class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(lambda: 0)
        lst = []
        newlst = []
        lst2 = []
        count = 0
        
        for i in nums:
            dic[i] += 1

        for key, value in dic.items():
            lst.append((value, key))

        lst.sort(reverse=True)

        for i in range(k):
            newlst.append(lst[i][1])
        return newlst