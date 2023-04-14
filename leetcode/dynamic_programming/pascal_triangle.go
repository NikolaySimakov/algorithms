package main

import "fmt"

func generate(numRows int) [][]int {
	if numRows == 1 {
		return [][]int{{1}}
	}
	arr := [][]int{{1}, {1, 1}}

	for i := 2; i < numRows; i++ {
		a := []int{1}
		for j := 0; j < len(arr[i-1])-1; j++ {
			a = append(a, arr[i-1][j]+arr[i-1][j+1])
		}
		a = append(a, 1)

		arr = append(arr, a)
	}

	return arr
}

func main() {

	// Example
	var n int = 5
	fmt.Println(generate(n))

}
