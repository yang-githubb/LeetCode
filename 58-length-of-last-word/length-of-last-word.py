class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()           
        if not s:              
            return 0
        parts = s.split(' ')      
        return len(parts[-1])   
