def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

def find_it_dict(seq):
    seq.sort()
    dict = {}
    
    for i in seq:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
            
    for key, val in dict.items():
        if val % 2 != 0:
            return key
                
    return None

