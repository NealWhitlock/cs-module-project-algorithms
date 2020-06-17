'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Create new list for storing products
    products = []
    # Loop through nums in arr
    for i in range(len(arr)):
        # Product variable to compute each product
        product = 1
        # Loop through nums in arr and multiply each of them except for the num in the first loop
        for j, num in enumerate(arr):
            # Make sure loops aren't pointing to same variable
            if i != j:
                # Multiply num
                product *= num
    # Append product to new list
        products.append(product)
    # Return new list
    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
