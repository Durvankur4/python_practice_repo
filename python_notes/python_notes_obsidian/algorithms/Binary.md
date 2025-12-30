log n 
1
```
def binarysearch(arr,target):
	L = 0
	R = len(arr)-1
	
	while L<=R:
		mid = L+R//2
		
		if target < mid:
			R = mid - 1
		elif target > mid:
			L = mid + 1
		else :
			return mid
	return -1
```
	