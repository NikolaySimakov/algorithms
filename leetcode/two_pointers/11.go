package two_pointers

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func Min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func maxArea(height []int) int {

	left := 0
	right := len(height) - 1
	maxSquare := 0

	for left < right {

		s := Min(height[left], height[right]) * (right - left)
		maxSquare = Max(s, maxSquare)

		if height[right] <= height[left] {
			right--
		} else {
			left++
		}
	}

	return maxSquare
}
