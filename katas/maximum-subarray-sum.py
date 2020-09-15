def max_sequence(arr):
    if all(i > 0 for i in arr):
        return sum(arr)
    elif all(i < 0 for i in arr):
        return 0
    else:
        n = len(arr)
        max_sum = -10000
        
        for left in range(0, n):
            running_sum = 0
            
            for right in range(left, n):
                running_sum += arr[right]
                
                max_sum = max(max_sum, running_sum)

        return max_sum
