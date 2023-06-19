func maxDistToClosest(seats []int) int {
	currentIndex, maxDistance := -1, 0

	for i := 0; i < len(seats); i++ {
		if seats[i] == 0 {
			continue
		}

		// handle the case when seats start with zeros 
		// [0, 0, 0, 1]
		if currentIndex == -1 {
			maxDistance = i
		} else {
			// handle the general case: between two '1's
			// [1, 0, 0, 1]
			maxDistance = max(maxDistance, (i-currentIndex)/2)
		}

		currentIndex = i
	}

	// handle the case when seats end with zeros 
	// [1, 0, 0, 0]
	return max(maxDistance, len(seats)-currentIndex-1)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}