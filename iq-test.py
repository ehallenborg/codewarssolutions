import collections, numpy

def iq_test(numbers):
    numbers = list(map(lambda x: int(x) % 2, list(numbers.split(" "))))

    a = numpy.array(numbers)
    
    return numbers.index(0) + 1 if (a == 1).sum() > 1 else numbers.index(1) + 1
