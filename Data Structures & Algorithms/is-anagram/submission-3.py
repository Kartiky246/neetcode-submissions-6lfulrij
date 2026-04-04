class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        for i in range(len(s)):
            if char_map.get(s[i]):
                char_map[s[i]] += 1
                if char_map[s[i]] == 0:
                    del char_map[s[i]]
            else:
                char_map[s[i]] = 1
            if char_map.get(t[i]):
                char_map[t[i]] -= 1
                if char_map[t[i]] == 0:
                    del char_map[t[i]]
            else:
                char_map[t[i]] = -1
        
        return len(char_map.keys()) == 0

        