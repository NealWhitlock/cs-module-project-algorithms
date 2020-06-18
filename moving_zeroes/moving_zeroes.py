'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Loop through items in array
#     for i, num in enumerate(arr):
#     # If item zero, pop off list and put at end
#         if num == 0:
#             arr.append(arr.pop(i))
#     # Return array
#     return arr

def moving_zeroes(arr):
    # Loop through each item in arr with pointers for a single pass
    # Left pointer set to first item
    left = 0
    # Right pointer set to last item
    right = len(arr) - 1
    # While left is less than right...
    while left < right:
        # Check if left is zero
        if arr[left] == 0:
            # If so, and right is non-zero
            if arr[right] != 0:
                # Swap locations of left and right
                arr[left], arr[right] = arr[right], arr[left]
        # If left is non-zero...
        else:
            # Increment left
            left += 1
        # If right is zero...
        if arr[right] == 0:
            # Decrement right
            right -= 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")