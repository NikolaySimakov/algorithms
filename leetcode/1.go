package main

import "fmt"

func contains(s []int, n int) bool {
	for _, v := range s {
		if v == n {
			return true
		}
	}

	return false
}

func indexOf[T comparable](collection []T, el T) int {
	for i, x := range collection {
		if x == el {
			return i
		}
	}
	return -1
}

func twoSum(nums []int, target int) []int {
	arr := []int{nums[0]}

	for i := 1; i < len(nums); i++ {
		if contains(arr, target-nums[i]) {
			return []int{i, indexOf(nums, target-nums[i])}
		} else {
			arr = append(arr, nums[i])
		}
	}

	return []int{}
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9

	fmt.Println(twoSum(nums, target))
}
