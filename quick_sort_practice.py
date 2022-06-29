"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    elements_greater = []
    elements_lower = []

    for element in array:
        if element > pivot:
            elements_greater.append(element)
        else:
            elements_lower.append(element)

    return quicksort(elements_lower) + [pivot] + quicksort(elements_greater)    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))