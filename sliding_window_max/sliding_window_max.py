'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Create new list to return
    new_list = []
    # Loop through nums in range len of nums - k + 1
    for i in range(len(nums)-k+1):
    # Slice a smaller list from i to i + k
    # Append this slice to a new list
        new_list.append(nums[i:i+k])
    # Loop through new list and replace each element with the max of the little list
    for i, lists in enumerate(new_list):
        new_list[i] = max(lists)
    # Return new list
    return new_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
