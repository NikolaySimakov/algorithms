package main

func search(nums []int, target int) int {
	var low int
	var high int = len(nums) - 1

	for low <= high {
		var mid int = low + (high-low)/2
		if nums[mid] == target {
			return mid
		}

		if nums[mid] >= nums[low] {
			if nums[mid] >= target && target >= nums[low] {
				high = mid - 1
			} else {
				low = mid + 1
			}
		} else {
			if nums[mid] <= target && target <= nums[high] {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}
	}

	return -1
}
