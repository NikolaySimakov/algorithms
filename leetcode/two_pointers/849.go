package twopointers

func maxDistToClosest(seats []int) int {
	currentIndex, maxDistance := -1, 0

	for i := 0; i < len(seats); i++ {
		if seats[i] == 0 {
			continue
		}

		if currentIndex == -1 {
			maxDistance = i
		} else {
			maxDistance = max(maxDistance, (i-currentIndex)/2)
		}

		currentIndex = i
	}

	return max(maxDistance, len(seats)-currentIndex-1)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
