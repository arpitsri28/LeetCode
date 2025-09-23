class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst_of_signatures = []
        groups = defaultdict(list)
        for words in strs:
            signature = {}
            for letters in words:
                if letters in signature:
                    signature[letters] += 1
                else:
                    signature[letters] = 1
            key = tuple(sorted(signature.items()))
            groups[key].append(words)
        
        return list(groups.values())

        
        
