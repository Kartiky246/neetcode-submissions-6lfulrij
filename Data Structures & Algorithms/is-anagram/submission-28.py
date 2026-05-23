class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict1 = {}
        char_dict2 = {}
        if (len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if(char_dict1.get(s[i])):
                char_dict1[s[i]] = char_dict1.get(s[i]) + 1
            else:
                char_dict1[s[i]] = 1
            if(char_dict2.get(t[i])):
                char_dict2[t[i]] = char_dict2.get(t[i]) + 1
            else:
                char_dict2[t[i]] = 1
        print(char_dict1)
        print(char_dict2)
        return char_dict1 == char_dict2