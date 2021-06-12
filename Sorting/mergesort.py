numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def mergeSort(arr):
  if len(arr) == 1:
    return arr
  half = int(len(arr)/2)-1 if len(arr) % 2 == 0 else int((len(arr)-1)/2)
  left = arr[:half+1]
  right = arr[half+1:]

  return merge2(
      mergeSort(left),
      mergeSort(right)
  )


def merge(left, right):
  merged = []
  index_left = 0
  index_right = 0
  while len(left) > index_left and len(right) > index_right:
    if left[index_left] < right[index_right]:
      merged.append(left[index_left])
      index_left += 1
    else:
      merged.append(right[index_right])
      index_right += 1
  if index_right < len(right):
    merged = merged + right[index_right:]
  elif index_left < len(left):
    merged = merged + left[index_left:]
  return merged


def merge2(left, right):
  merged = []
  index_left = 0
  index_right = 0
  while len(left) > index_left and len(right) > index_right:
    if left[index_left] <= right[index_right]:
      merged.append(left[index_left])
      index_left += 1
    else:
      merged.append(right[index_right])
      index_right += 1
  merged += left[index_left:]
  merged += right[index_right:]
  return merged


answer = mergeSort(numbers)
print(answer)
