class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {
            'I':1,
            'V':5,
            'X':10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        total_val = 0
        n = len(s)

        for i in range(n):
            if i<n-1 and val[s[i]] < val[s[i+1]]:
                total_val -= val[s[i]]
            else:
                total_val += val[s[i]]
        return total_val
        