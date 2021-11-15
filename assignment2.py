import csv

with open ("assignment2_file.csv") as csv_file:
    csv_reader = csv.reader (csv_file)
    list1 = list(csv_reader)
    print(list1)

#tupil 
with open  ("assignment2_file.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    tuple1 = tuple(csv_reader)
    print(tuple1)

#dictionary
with open ("assignment2_file.csv") as csv_file:
    csv_reader = csv.reader (csv_file)
    dictionary1 = csv.DictReader(csv_reader)
    list_of_dict = list(dictionary1)
    print(list_of_dict)

#array
with open ("assignment2_file.csv") as csv_file:
     file_read = csv.reader(csv_file)
     array1 = list(file_read)
     print(array1)

#list
with open ("assignment2_file.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    lists_from_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)
print(lists_from_csv)

#set
with open ("assignment2_file.csv") as csv_file:
   csv_reader = csv.reader(csv_file)
   set1 = set(csv_file)
   print(set1)

#insertion sort
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

#merge sort
def merge_sort(tupil):
    # The last tupil split
    if len(tupil) <= 1:
        return tupil
    mid = len(tupil) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(tupil[:mid]), merge_sort(tupil[mid:])

    # Merge each side together
    return merge(left, right, tupil.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
     
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

def sort(array=[12,4,5,6,7,3,1,15]):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
       
        return sort(less)+equal+sort(greater) 
   
    else:  
        return list

def sub_partition(array, start, end, idx_pivot):

    'returns the position where the pivot winds up'

    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

def quicksort(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = (start, end)
    i = sub_partition(array, start, end, idx_pivot)
    
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)

with open('assignment2_file.csv', 'r') as read_obj:
    csv_reader = csv_reader(read_obj)
    for row in csv_reader:
        print(row)