# Greedy Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index has the minimum
        min_index = i

        # Greedily search for the smallest element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Debug output to show steps
        print(f"Step {i+1}: {arr}")

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
