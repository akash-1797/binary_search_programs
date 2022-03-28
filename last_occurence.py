def binary_search(arr,key):
  res = 'not found'
  low = 0
  high = len(arr)-1
  while(low <= high):
    mid = low + (high-low)//2
    if arr[mid] == key:
      res =  mid
      low = mid +1
    elif arr[mid] > key:
      high = mid -1
    else:
        low = mid +1
  return res 

arr = [12,32,32,32,44,56,79]
key = 32 
print(binary_search(arr,key))


