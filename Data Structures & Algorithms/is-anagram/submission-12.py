class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counts , countt = defaultdict(lambda: 0), defaultdict(lambda: 0)

        for x,y in zip_longest(s, t, fillvalue="-"):
            counts[x] += 1
            countt[y] += 1

        return counts == countt