# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    for i in range(0, len(arr)):
        cur_index = i
        
        if i == 0:
          pass
        else:
          while cur_index > 0:
            if arr[cur_index] < arr[cur_index-1]:
              smallest_index = arr[cur_index]
              biggest_index = arr[cur_index-1]
              arr[cur_index] = biggest_index
              arr[cur_index-1] = smallest_index
              cur_index -= 1
            else:
              break

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

  if len(arr) == 0:
    return arr

  swap = True

  while swap:
    count = 0
    for i in range(0, len(arr)):
      if i == (len(arr) - 1):
        if count == 0:
          swap = False

      elif arr[i] > arr[i+1]:
        biggest_index = arr[i]
        smallest_index = arr[i+1]
        arr[i] = smallest_index
        arr[i+1] = biggest_index
        count += 1
  return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
