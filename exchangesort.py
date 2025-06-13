# This is an implementation of the exchange sort algorithm in Python.
def exchange_sort(arr) -> None:
    """
    Sorts an array in place using the exchange sort algorithm.
    
    :param arr: List of elements to be sorted.
    """
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                # Swap the elements
                arr[i], arr[j] = arr[j], arr[i]