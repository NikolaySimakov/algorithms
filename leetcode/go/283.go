package main

import (
	"fmt"
)

func moveZeroes(nums []int) {
	a := 0
	b := len(nums) - 1

	for {
		if a == b || a > b {
			break
		}

		if nums[a] == 0 {
			nums = append(nums[:a], nums[a+1:]...)
			nums = append(nums, 0)
			b--
		} else {
			a++
		}
	}
}

func main() {
	numbers := []int{0, 1, 0, 3, 12}
	moveZeroes(numbers)
	fmt.Println(numbers)
}
