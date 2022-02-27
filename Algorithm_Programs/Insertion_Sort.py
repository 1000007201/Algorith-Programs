def insertion_sort(arr):

    for i in range(1, len(arr)):
        val = arr[i]

        j = i-1
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

    return arr


if __name__ == "__main__":
    sample_string = "nishantsharma"
    arr = [i for i in sample_string]
    print(f"Unsorted List:\n{arr}")
    print(f"Sorted List:\n{insertion_sort(arr)}")

