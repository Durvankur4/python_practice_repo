time complexity O(n^2)
space complexity O(1) "in place sort"

```
def bubble_sort(arr):
	length = len(arr)
	flag = True
	
	while flag:
		flag = False
		for i in range(1,length):
			if arr[i-1] > arr[i]:
				flag = True
				arr[i-1], arr[i] = arr[i], arr[i-1]
	return arr		
```

there are more ways to optimize this