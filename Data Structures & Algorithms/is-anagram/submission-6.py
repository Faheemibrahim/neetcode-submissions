class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = []
        lst2 = []
        
        for x, y in zip_longest(s, t, fillvalue="-"):
            lst1.append(x)
            lst2.append(y)
        
        a = sorted(lst1)
        b = sorted(lst2)

        for a,b in zip_longest(a,b, fillvalue="-"):
            if a != b:
                return False
        return True

