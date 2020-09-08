def list_squared(m, n):
    squared = []
    
    for i in range(m, n+1):
        j = divisors(i)
        j.sort()
        if int(sum([number ** 2 for number in j])**0.5 + 0.5) ** 2 == sum([number ** 2 for number in j]) and i not in squared:
            squared.append( [i, sum([number ** 2 for number in j])] )

    return squared

def divisors(n):
    divs = [1]
    for i in range(2,int((n**0.5)+1)):
        if n % i == 0:
            divs.extend([int(i), int(n/i)])
    divs.extend([n])
    return list(set(divs))