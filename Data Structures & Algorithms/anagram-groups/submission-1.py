class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            sorted_chars = ''.join(sorted(s))

            if sorted_chars not in anagram_map:
                anagram_map[sorted_chars] = []
            anagram_map[sorted_chars].append(s)
        
        return list(anagram_map.values())


        
            