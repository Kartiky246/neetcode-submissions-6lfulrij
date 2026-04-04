class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in range(len(strs)):
            mapKey = ''.join(sorted(strs[i]))
            if mapKey in anagram_map:
                list = anagram_map[mapKey]
                list.append(strs[i])
                anagram_map[mapKey] = list
            else:
                anagram_map[mapKey] = [strs[i]]
        return anagram_map.values()