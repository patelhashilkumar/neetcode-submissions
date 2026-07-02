class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            rag = ''.join(sorted(s))
            res[rag].append(s)
        return list(res.values())