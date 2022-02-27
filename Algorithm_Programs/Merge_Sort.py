
def merge_sort(array):
    if len(array) > 1:

        #  mid is the point where the array is divided into two subarrays
        mid = len(array)//2
        array_1 = array[:mid]
        array_2 = array[mid:]

        # Sort the two halves
        merge_sort(array_1)
        merge_sort(array_2)

        i = j = k = 0

        # Until we reach either end of either array_1 or array_2, pick larger among
        # elements array_1 and array_2 and place them in the correct position at A[p..mid]
        while i < len(array_1) and j < len(array_2):
            if array_1[i] < array_2[j]:
                array[k] = array_1[i]
                i += 1
            else:
                array[k] = array_2[j]
                j += 1
            k += 1

        # When we run out of elements in either array_1 or array_2,
        # pick up the remaining elements and put in A[p..mid]
        while i < len(array_1):
            array[k] = array_1[i]
            i += 1
            k += 1

        while j < len(array_2):
            array[k] = array_2[j]
            j += 1
            k += 1


# Print the array
def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    merge_sort(array)

    print("Sorted array is: ")
    print_list(array)