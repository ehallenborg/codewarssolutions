import collections

def sort_by_name(arr):
    # 0 - 999
    units ={
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
        9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
        }
        
    tens = {1: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    
    scales = "hundred"
    
    words = {}
    sorted_arr = []
    
    for i in range(len(arr)):
        if arr[i] < 20:
            words[units[arr[i]]] = arr[i]
        elif arr[i] < 100 and arr[i] > 20:
            words[(tens[int(str(arr[i])[0])] + units[int(str(arr[i])[1])])] = arr[i]
        else:
            words[(units[int(str(arr[i])[1])] + ' hundred ' + tens[int(str(arr[i])[0])] + units[int(str(arr[i])[1])])] = arr[i]  
        
    sorted_dict = collections.OrderedDict(sorted(words.items()))

    for value in sorted_dict.values():
        sorted_arr.append(value)
        
    return sorted_arr