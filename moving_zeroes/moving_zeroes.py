'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Loop through items in array
    for i, num in enumerate(arr):
    # If item not zero, pop off list and insert in array at index 0
        if num != 0:
            arr.insert(0, arr.pop(i))
    # Return array
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")