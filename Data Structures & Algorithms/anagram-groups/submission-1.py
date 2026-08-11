class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        words = []

        for word in strs:
            words.append(sorted(word))


        for keys, values in zip(strs, words):
            new_values = tuple(values)

            if new_values in d:
                d[new_values].append(keys)
            else:
                d[new_values] = [keys]

        final = list(d.values())

        return final
