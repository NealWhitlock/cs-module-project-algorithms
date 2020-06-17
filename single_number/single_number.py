'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Create a set
    num_set = set()
    # Loop through items in the list
    for item in arr:
        # Check if item is in set,
        if item not in num_set:
            # If not, add to set
            num_set.add(item)
        else:
            # If so, remove from set
            num_set.remove(item)
    
    # Return the only value in the set
    return num_set.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")