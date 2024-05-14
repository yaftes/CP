def longest_equal_indexes(arr1, arr2):
    # Initialize the longest equal index and current equal index
    longest_index = -1
    current_index = -1
    
    # Iterate through the arrays
    for i in range(min(len(arr1), len(arr2))):
        # If elements at the current index are equal, update the current equal index
        if arr1[i] == arr2[i]:
            current_index = i
        # If elements are not equal, update the longest equal index
        else:
            longest_index = max(longest_index, current_index)
    
    # Return the longest equal index
    return longest_index

# Example usage:
arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [1, 2, 3, 4, 5, 8, 9]

longest_index = longest_equal_indexes(arr1, arr2)
print("Longest equal index:", longest_index)
