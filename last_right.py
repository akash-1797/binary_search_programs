def left_and_right(arr,key,leftbais):
  res = -1
  low = 0 
  high = len(arr)-1
  while(low <=high):
    mid = low + (high -low)//2
    if arr[mid] > key:
      high = mid - 1
    elif arr[mid] < key:
      low = mid+1
    else:
      res = mid 
      if leftbais:
        high = mid - 1
      else:
        low = mid +1
  return res

arr = [4,5,6,11,11,11,45,56]
key= 11
left = left_and_right(arr,key,True)
right = left_and_right(arr,key,False)
print(left,right)
