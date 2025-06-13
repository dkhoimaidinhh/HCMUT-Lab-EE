# This is an implementation of the bubble sort algorithm in Python.
def bubble_sort(arr) -> None:
    """
    Sorts an array in place using the bubble sort algorithm.
    
    :param arr: List of elements to be sorted.
    """
    n = len(arr)
    
    for i in range(n):
        # Track if a swap was made
        swapped = False
        
        for j in range(0, n - i - 1):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break