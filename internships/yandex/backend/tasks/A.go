package main

import "fmt"

func equalizeReservoirs(n int, nums []int) int {

	maxValue, minValue := nums[0], nums[0]

	for i := 1; i < n; i++ {
		if nums[i] < nums[i-1] {
			return -1
		}
		if maxValue < nums[i] {
			maxValue = nums[i]
		}
		if minValue > nums[i] {
			maxValue = nums[i]
		}
	}

	return maxValue - minValue
}

func main() {
	var n int
	fmt.Scan(&n)

	arr := make([]int, n)

	for i := 0; i < len(arr); i++ {
		fmt.Scan(&arr[i])
	}

	res := equalizeReservoirs(n, arr)
	fmt.Println(res)
}
