package main

// Two Sum II - Input Array Is Sorted

func twoSum(numbers []int, target int) []int {
	low := 0
	high := len(numbers) - 1

	for numbers[low]+numbers[high] != target && low < high {
		if (target - numbers[low]) < numbers[high] {
			high--
		} else if (target - numbers[high]) > numbers[low] {
			low++
		}
	}

	return []int{low + 1, high + 1}
}
