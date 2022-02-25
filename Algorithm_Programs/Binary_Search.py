# Returns index of element in arr if present, else -1
def binary_search(arr, low, high, element):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == element:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > element:
            return binary_search(arr, low, mid - 1, element)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, element)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
element = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, element)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")