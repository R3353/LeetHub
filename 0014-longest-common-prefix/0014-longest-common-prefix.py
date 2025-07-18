class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ''
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or strs[0][i] != word[i]:
                    return answer
            answer += strs[0][i]
        return answer    
        