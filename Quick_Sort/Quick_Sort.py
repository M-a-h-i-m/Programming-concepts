def quick_sort(arr, low, high):
  if low < high:  
   pi = partition(arr, low, high)  # Find pivot index after partition
   quick_sort(arr, low, pi - 1)    # Recursively sort the two halves
   quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
  pivot = arr[high]  # choose the last element as pivot
  i = low - 1        # pointer for smaller element

  for j in range(low, high):
      if arr[j] < pivot:
          i += 1
          temp = arr[i]
          arr[i] = arr[j]
          arr[j] = temp 
          print(i,j,arr)

  temp = arr[i + 1]
  arr[i + 1] = arr[high]
  arr[high] = temp            # place pivot in correct position
  return i + 1



data = [8, 3, 1, 7, 0, 10, 2]
quick_sort(data, 0, len(data) - 1)
