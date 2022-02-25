def bubble_sort(arr):
    """
    It Takes Unsorted array and returns Sorted Array.
    :param arr: Unsorted Array
    :return: Sorted Array
    """
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == "__main__":

    arr = [7, 15, 65, 41, 21, 24, 12]
    print(f"Unsorted Array:\n{arr}")
    print(f"Sorted Array:\n{bubble_sort(arr)}")
