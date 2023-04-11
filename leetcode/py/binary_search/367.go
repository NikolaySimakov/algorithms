func peakIndexInMountainArray(arr []int) int {
    low := 1
    high := len(arr) - 2
    
    for low <= high {
        mid := low + (high - low)/2

        if arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1] {
            return mid
        } else {
            if arr[mid] > arr[mid - 1] {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
    }

    return low
}