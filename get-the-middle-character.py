def get_middle(s):
    if len(s) == 1 or len(s) == 2:
        return s
    else:
        if (len(s) % 2 != 0):
            return (s[len(s)//2])
        else:
            return (s[len(s)//2 -1 :len(s)//2 + 1])
        
    