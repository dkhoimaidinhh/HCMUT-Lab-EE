# Linear Search Algorithm takes O(n)
# Binary Search Algorithm takes O(log n) - Most Easy and Efficient
# Jump Search Algorithm takes O(√n)
# Interpolation Search Algorithm takes O(log log n)
# Exponential Search Algorithm takes O(log n)

# This is an implementation of the binary search algorithm in Python.
def binary_search(arr, target) -> int:
    """
    Performs binary search on a sorted array to find the index of the target element.
    
    :param arr: List of sorted elements.
    :param target: Element to search for in the array.
    :return: Index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # Target was not found in the array
    return -1

# This is an implementation of the linear search algorithm in Python.
def linear_search(arr, target) -> int:
    """
    Performs linear search on an array to find the index of the target element.
    
    :param arr: List of elements.
    :param target: Element to search for in the array.
    :return: Index of the target element if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# This is an implementation of the jump search algorithm in Python.
def jump_search(arr, target) -> int:
    """
    Performs jump search on a sorted array to find the index of the target element.
    
    :param arr: List of sorted elements.
    :param target: Element to search for in the array.
    :return: Index of the target element if found, otherwise -1.
    """
    n = len(arr)
    step = int(n**0.5)  # Optimal jump size
    prev = 0
    
    # Finding the block where the target may be present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    
    # Linear search within the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
            
    if arr[prev] == target:
        return prev
    
    return -1

# This is an implementation of the interpolation search algorithm in Python.
def interpolation_search(arr, target) -> int:
    """
    Performs interpolation search on a sorted array to find the index of the target element.
    
    :param arr: List of sorted elements.
    :param target: Element to search for in the array.
    :return: Index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Estimate position using interpolation formula
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1