class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char_map[s[i]] = char_map.get(s[i],0) + 1
            char_map[t[i]] = char_map.get(t[i],0) - 1
            if(char_map.get(s[i]) == 0):
                del char_map[s[i]]
            if(char_map.get(t[i]) == 0):
                del char_map[t[i]]
        return len(char_map) == 0