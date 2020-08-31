def move_zeros(array):
    #zeroes = [0] * (sum(1 for x in list(array) if x is 0))
    #array = list(filter(lambda x : x is not 0, array))
    zeroes = list(filter(lambda a: a == 0 and not isinstance(a, bool), array))
    array = list(filter(lambda a: a != 0 or isinstance(a, bool), array))

    return array + zeroes
