package main

func getMax(piles []int) int {
	var max int = piles[0]
	for _, v := range piles {
		if v > max {
			max = v
		}
	}
	return max
}

func minEatingSpeed(piles []int, h int) int {

	low := 1
	high := getMax(piles)

	for low < high {
		mid := low + (high-low)/2
		count := 0
		for _, v := range piles {
			count += (v-1)/mid + 1
		}

		if count <= h {
			high = mid
		} else {
			low = mid + 1
		}
	}

	return low
}
