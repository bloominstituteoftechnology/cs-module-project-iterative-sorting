# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
	amountSorted = 0									# amount of sorted members
	sui = -1											# Smallest unsorted index

	while amountSorted != len(arr):
		for i in range(0+amountSorted, len(arr)):		# Start at unsorted value
			if sui == -1 or arr[i] < arr[sui]:		    # If we find a new smallest unsorted value
				sui = i									# set smallestUnsorted to arr[i]

		# Add smallest found to end of sorted
		arr.insert(amountSorted, arr[sui])				# Add the smallest found to the sorted
		arr.pop(sui+1)									# Remove newly-sorted from unsorted
		amountSorted += 1								# Inc amount sorted
		sui = -1										# Reset sui

	return arr

def bubble_sort(arr):
	didSwap = True

	# Loop through array
	while didSwap:
		# Reset swap
		didSwap = False
	
		# Loop through arr
		for i in range(0, len(arr)-1):

			# Check bounds & compare
			if i+1 != len(arr) and arr[i] > arr[i+1]:
				# Swap
				arr[i], arr[i+1] = arr[i+1], arr[i]
				didSwap = True
	return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
