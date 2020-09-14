def printer_error(s):
    alphabet = set(list(map(chr, range(97, 110))))
    set_s = set(s)
    diff = 0
    
    if set_s.issubset(alphabet):
        return "0/" + str(len(s))
    else:
        for i in s:
            if i not in alphabet:
                diff += 1
        
    return str(diff) + "/" + str(len(s))

def printer_error_one_liner(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

from re import sub
def printer_error_with_re(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
