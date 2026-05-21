class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_exits = dict()
        char_exits2 = dict()
        for c in s:
            if c not in char_exits:
                char_exits[c] = 1
            else:
                char_exits[c] += 1
        for c in t:
            if c not in char_exits2:
                char_exits2[c] = 1
            else:
                char_exits2[c] += 1
        return (char_exits == char_exits2)