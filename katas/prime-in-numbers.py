def primeFactors(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret

def primeFactorsfailedfirstattempt(n):
    prime = {}
    string = ''

    if n % 2 == 0:
        prime[2] = 1
        n = n / 2
    while n % 2 == 0: 
        prime[2] += 1
        n = n / 2
    
    for i in range(3, int((n**0.5)+1), 2): 
        while n % i== 0: 
            if i not in prime.keys():
                prime[i] = 1
                n = n / i
            else:
                prime[i] += 1
                n = n / i
                
    if n > 2: 
        prime[i] = 1 
            
    for key, value in prime.items():
        if value > 1:
            string = string + '(' + str(key) + '**' + str(value) + ')'
        else:
            string = string + '(' + str(key) + ')'
            
    return string

def primeFactorsfirstsuccessfulattempt(n):
    i = 2
    prime = {}

    while n/i != 1:
      if n%i == 0:
        if i in prime:
            prime[i] = prime[i]+1
        else:
            prime[i] = 1
        n = n/i
      else:
        i+=1

    if i in prime:
        prime[i] = prime[i]+1
    else:
        prime[i] = 1
    
    t = ''
    prime = sorted(prime.items(),key = lambda a:a[0])

    for key in prime:
        if key[1] == 1:
           t = t + '('+str(key[0]) +')'
        else:
           t = t + '(' +str(key[0]) + '**' + str(key[1]) + ')'
    return t