class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            s_word = tuple(sorted(word))
            if s_word in seen:
                seen[s_word].append(word)
            else:
                seen[s_word] = [word]
        return list(seen.values())