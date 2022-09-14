def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        val = 0
        while i < len(s):
            if s[i] == 'I':
                if i+1 < len(s):
                    if s[i+1] == 'V':
                        val += 4
                        i += 2
                    elif s[i+1] == 'X' : 
                        val += 9
                        i += 2
                    else:
                        val += 1
                        i += 1
                    
            if s[i] == 'X':
                if i+1 < len(s):
                    if s[i+1] == 'L':
                        val += 40
                        i += 2
                    elif s[i+1] == 'C':
                        val += 90
                        i += 2                 
                    else:
                        val += 10
                        i += 1
            
            if s[i] == 'C':
                if i+1 < len(s):
                    if s[i+1] == 'D':
                        val += 400
                        i += 2
                    elif s[i+1] == 'M':
                        val += 900
                        i += 2                 
                    else:
                        val += 100
                        i += 1
                    
romanToInt("III")