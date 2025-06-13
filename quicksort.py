# This is an implementation of the quicksort algorithm in Python.
def quicksort(arr) -> None:
    """
    Sorts an array in place using the quicksort algorithm.
    
    :param arr: List of elements to be sorted.
    """
    def _quicksort(low, high):
        if low < high:
            # Partition the array
            pivot_index = partition(low, high)
            # Recursively sort the partitions
            _quicksort(low, pivot_index - 1)
            _quicksort(pivot_index + 1, high)

    def partition(low, high):
        # Choose the rightmost element as pivot
        pivot = arr[high]
        i = low - 1  # Pointer for the smaller element
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than or equal to pivot
        
        # Swap the pivot element with the element at i + 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quicksort(0, len(arr) - 1)