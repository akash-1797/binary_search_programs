def firstIndex(self, arr, n):
        low = 0
        mid= 0
        high = len(arr)-1
        res = -1
        while(low <= high):
            mid = low + (high-low)//2
            if arr[mid] == 1:
                res = mid
                high = mid-1
            else:
                low = mid +1
        return res
