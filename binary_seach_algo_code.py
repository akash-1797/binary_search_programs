def binary_search(arr,key,debug = False):
  low = 0
  high = len(arr)-1
  while(low <= high):
    mid = low + (high-low)//2
    if debug:
      print('low',low)
      print('high',high)
      print('mid',mid)
    if arr[mid] == key:
      return mid 
    elif arr[mid] > key:
      high = mid -1
    else:
      low = mid + 1
  return "not found"

arr = [12,34,65,77,100,101,801]
key = 101
print(binary_search(arr,key,True))

