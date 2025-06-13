# This is an implementation of the shell sort algorithm in Python.
def shell_sort(arr) -> None:
    """
    Sorts an array in place using the shell sort algorithm.
    
    :param arr: List of elements to be sorted.
    """
    n = len(arr)
    gap = n // 2  

    while gap > 0:
        for i in range(gap, n):
            currentValue = arr[i]
            j = i
            
            # Shift elements of arr[0..i-gap], that are greater than currentValue,
            # to one position ahead of their current position
            while j >= gap and arr[j - gap] > currentValue:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = currentValue
        
        gap //= 2

# Example usage:
if __name__ == "__main__":
    sample_array = [12, 34, 54, 2, 3]
    print("Original array:", sample_array)
    shell_sort(sample_array)
    print("Sorted array:", sample_array)
