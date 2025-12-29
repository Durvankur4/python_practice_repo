time complexity : O(n^2)
space complexity  :  O(1)
```
def selection(arr):
	length = len(arr)
	for i in range(length):
		min_index = i
		for j in range(i+1,length):
			if arr[min_index] > arr[j]
				min_index = j
			arr[min_index], arr[j] = arr[j], arr[min_index]  
			
```