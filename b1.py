
array = []

# def max_sum_subarray(array):

#     best_sum = 0
#     current_sum - 0



def max_subarray(numbers):
    """Find a contiguous subarray with the largest sum."""
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end



print(max_subarray([49,13,-27,53,-31,11,-42,-93,76,83,-89,96,90,89,-40,51,-41,20,99,98,-93,80,87,-75,9,72,71,33,-85,-11]))

# our sub array : [49,13,-27,53,-31,11,-42,-93,76,83,-89,96,90,89,-40,51,-41,20,99,98,-93,80,87,-75,9,72,71,33,-85,-11]