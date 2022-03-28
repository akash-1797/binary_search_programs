def binary_search(arr,key):
  low = 0
  high = len(arr)-1
  while(low <= high):
    mid = low + (high-low)//2
    if arr[mid] == key:
      return mid 
    elif arr[mid] > key:
      low = mid+1
    else:
      high = mid - 1
  return "not found"

arr = [9,7,5,4,3,1]
key = 3
print(binary_search(arr,key))


