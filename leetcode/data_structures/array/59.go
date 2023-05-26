package main

import "fmt"

func generateMatrix(n int) [][]int {

	matrix := make([][]int, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int, n)
	}

	count := 1

	for i, j := 0, n-1; i <= j; i++ {

		for a := i; a <= j; a++ {
			matrix[i][a] = count
			count++
		}

		for a := i + 1; a <= j; a++ {
			matrix[a][j] = count
			count++
		}

		for a := j - 1; a >= i; a-- {
			matrix[j][a] = count
			count++
		}

		for a := j - 1; a > i; a-- {
			matrix[a][i] = count
			count++
		}

		j--
	}

	return matrix
}

func main() {
	m := generateMatrix(4)
	fmt.Println(m)
}
