class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # [0, 0, 0, ] ... upto 26th
            # app, ppa, pap => [1,0,...2,..0] all will have this key
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            # [1,0,...2,..0] all will have this key
            # now use this key to store the app, ppa, pap in the dict
            # list should be converted to tuple to store them as keys in dict
            res[tuple(key)].append(s)
        
        return list(res.values())


