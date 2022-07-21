def find_ceil(arr,x):
  n = len(arr)
  low = 0
  high = n-1
  res = -1
  while(low <= high):
    mid = low + (high-low)//2
    if arr[mid] == x:
      return arr[mid]
    elif arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      res = arr[mid]
      high = mid - 1
  return res


arr = [1,2,8,10,11,12,19]
x = 5
print(find_ceil(arr,x))

