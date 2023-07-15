package main

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxSubArray(nums []int) int {
	var n int = len(nums)
	var acc, max, min int = nums[0], nums[0], Min(0, nums[0])

	for i := 1; i < n; i++ {
		acc += nums[i]
		max = Max(max, acc-min)
		min = Min(min, acc)
	}

	return max
}
