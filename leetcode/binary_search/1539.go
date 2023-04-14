package main

import "fmt"

// if arr[-1] <= len of arr returns len of arr + k
// if arr[0] > k returns k
// if k missing element within array,
// => binary search => finds element that has minimum difference between value and index + 1
// this difference should be equal to k
// returns arr[low] - (arr[low] - low - k - 1 + 1) = low + k

func findKthPositive(arr []int, k int) int {

	if arr[len(arr)-1] <= len(arr) {
		return len(arr) + k
	} else if arr[0] > k {
		return k
	}

	low := 0
	high := len(arr) - 1

	for high >= low {
		mid := low + (high-low)/2

		if arr[mid]-mid-1 >= k {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return low + k
}

func main() {

	// example
	arr := []int{5, 6, 7, 8, 9}
	k := 9

	number := findKthPositive(arr, k)

	fmt.Println(number)
}
