'''
Input: a List of integers
Returns: a List of integers
'''
# def product_of_all_other_numbers(arr):
#     # Create new list for storing products
#     products = []
#     # Loop through nums in arr
#     for i in range(len(arr)):
#         # Product variable to compute each product
#         product = 1
#         # Loop through nums in arr and multiply each of them except for the num in the first loop
#         for j, num in enumerate(arr):
#             # Make sure loops aren't pointing to same variable
#             if i != j:
#                 # Multiply num
#                 product *= num
#     # Append product to new list
#         products.append(product)
#     # Return new list
#     return products

'''
Using two lists in sequential loops to get products
'''
def product_of_all_other_numbers(arr):
    # Length of arr is used a lot so store as variable n
    n = len(arr)

    # Two lists needed for intermediate multiplication
    # One needed for final products; each being of length n
    left = [0]*n
    right = [0]*n
    products = [0]*n

    # For left list set the first index to 1
    # For right list set last index to 1
    left[0] = 1
    right[-1] = 1

    # Loop through arr beginning at the second indices of left and arr
    # Multiply each incoming element from arr by the prior element in left
    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]
    
    # Loop through arr working backwards this time
    # Multiply each incoming element from arr by the element ahead of if in right
    for j in range(n-2, -1, -1):
        right[j] = right[j+1] * arr[j+1]
    
    # With these two lists set up loop through products and make each element
    # the product of the respective elements from left and right
    for k in range(n):
        products[k] = left[k] * right[k]
    
    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
