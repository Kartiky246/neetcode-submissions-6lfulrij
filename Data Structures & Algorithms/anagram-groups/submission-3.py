class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for _, str in enumerate(strs):
            key = ''.join(sorted(str))
            anagram_list = anagram_map.get(key, [])
            anagram_list.append(str)
            anagram_map[key] = anagram_list
        return list(anagram_map.values())