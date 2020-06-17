'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    count_list = []

    def helper_function(n, count_list):

      if n >= 3:
        helper_function(n-3, count_list)
      if n >= 2:
        helper_function(n-2, count_list)
      if n >= 1:
        helper_function(n-1, count_list)
      if n == 0:
        count_list.append(1)

      return len(count_list)

    count = helper_function(n, count_list)

    return count

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 15

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
