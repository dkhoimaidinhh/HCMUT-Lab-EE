#This is an implementation of the selection sort algorithm in Python.
def selection_sort(arr) -> None:
    """
    Sorts an array in place using the selection sort algorithm.
    
    :param arr: List of elements to be sorted.
    """
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]