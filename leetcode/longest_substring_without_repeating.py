class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        indexes = {}
        longest = 0
        i = 0

        while i < len(s):
            if s[i] not in chars:
                chars.append(s[i])
                indexes[s[i]] = i
                i += 1
            else:
                if len(chars) > longest:
                    longest = len(chars)
                chars = []
                i = indexes[s[i]] + 1

        return longest


sol = Solution()
sol.lengthOfLongestSubstring("abcabcbb")
