# This is an implementation of the merge sort algorithm in Python.
def mergesort(arr) -> None:
    """
    Sorts an array in place using the merge sort algorithm.
    
    :param arr: List of elements to be sorted.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]        # Dividing the elements into 2 halves
        R = arr[mid:]

        mergesort(L)  # Sorting the first half
        mergesort(R)  # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage:
if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_array)
    mergesort(sample_array)
    print("Sorted array:", sample_array)