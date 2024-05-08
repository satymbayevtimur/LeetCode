# First approach

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefixLength = len(prefix)

        for s in strs[1:]:
            while prefix != s[0:prefixLength]:
                prefixLength -= 1

                if prefixLength == 0:
                    return ''

                prefix = prefix[0:prefixLength] 

        return prefix

# Second approach

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        sortedStrings = sorted(strs)
        firstCharacter = sortedStrings[0]
        lastCharacter = sortedStrings[-1]

        for i in range(min(len(firstCharacter), len(lastCharacter))):
            if (firstCharacter[i] != lastCharacter[i]):
                return result
            
            result += firstCharacter[i]

        return result
