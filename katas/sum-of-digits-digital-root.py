'''
my original one
'''
def digital_root(n):
    string = str(n)
    sum = summing(string)    
        
    return sum

def summing(n):
    sum = 0
    
    for i in range(len(n)):
        sum += int(n[i])
    
    return sum if len(str(sum)) < 2 else summing(str(sum))

'''
one line clever solution
'''
def digital_root_one_line(n):
    return n%9 or n and 9 

'''
second attempt
'''
def digital_root_second_sol(n):
    while n>10:
        n = sum([int(i) for i in str(n)])
    return n if n != 10 else 1
