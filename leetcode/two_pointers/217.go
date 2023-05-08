package main

import "fmt"

func maxSubArray(nums []int) int {
	var i int = 0
	var j int = len(nums) - 1

	for {
		var _sum int = 0

		for _, v := range nums[i:j] {
			_sum += v
		}

		if _sum > _sum-nums[i] {
			i++
		} else if _sum > _sum-nums[j] {
			j--
		} else {
			return _sum
		}
	}
}

func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println(maxSubArray(nums))
}
