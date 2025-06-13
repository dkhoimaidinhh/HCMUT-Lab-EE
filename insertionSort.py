# This is an implementation of the insertion sort algorithm in Python.
def insertion_sort(arr) -> None:
    """
    Sorts an array in place using the insertion sort algorithm.
    
    :param arr: List of elements to be sorted.
    """
    for i in range(1, len(arr)):
        currentValue = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and currentValue < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = currentValue

# This take O(n^2) time in the worst case, which occurs when the array is sorted in reverse order.
