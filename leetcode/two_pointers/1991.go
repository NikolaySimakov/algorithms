package main

func sum(nums []int, start int, end int) int {
	s := 0
	for i := start; i < end; i++ {
		s += nums[i]
	}
	return s
}

func findMiddleIndex(nums []int) int {
	s1 := 0
	s2 := sum(nums, 1, len(nums))

	if s1 == s2 {
		return 0
	}

	for i := 1; i < len(nums); i++ {

		s1 += nums[i-1]
		s2 -= nums[i]

		if s1 == s2 {
			return i
		}
	}

	return -1
}
