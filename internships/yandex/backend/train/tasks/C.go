package main

import "fmt"

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func distance(i, m, n int, arr []int) int {

	count := 0

	r := i + 1
	l := i - 1

	for j := 0; j < m; j++ {
		fmt.Println(r, l)
		if n > r && l >= 0 {
			if abs(arr[i]-arr[l]) >= abs(arr[i]-arr[r]) {
				count += abs(arr[i] - arr[r])
				r++
			} else {
				count += abs(arr[i] - arr[l])
				l--
			}
		} else if n <= r {
			count += abs(arr[i] - arr[l])
			l--
		} else if l < 0 {
			count += abs(arr[i] - arr[r])
			r++
		}
	}

	return count
}

func main() {
	var n int
	var m int

	fmt.Scan(&n)
	fmt.Scan(&m)

	arr := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	distances := make([]int, n)
	for i := 0; i < n; i++ {
		distances[i] = distance(i, m, n, arr)
	}

	fmt.Println(distances)
}
