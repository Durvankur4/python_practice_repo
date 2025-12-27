time complexity : O(n^2)
space complexity : O(1) in place sort
```
def insertion(arr):
	length = len(arr)
	for i in range(1,length):
		for j in range(i,0,-1):
			if arr[j-1] > arr[j]:
				arr[j-1],arr[j] =  arr[j],arr[j-1]
			else:
				break

```