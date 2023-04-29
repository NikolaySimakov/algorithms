package main

// horizontal mirror
func mirrorX(matrix [][]int) {
	row := len(matrix[0])
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < row/2; j++ {
			matrix[i][j], matrix[i][row-j-1] = matrix[i][row-j-1], matrix[i][j]
		}
	}
}

// vertical mirror
func mirrorY(matrix [][]int) {
	col := len(matrix)
	for i := 0; i < col; i++ {
		for j := 0; j < len(matrix[0])/2; j++ {
			matrix[i][j], matrix[col-i-1][j] = matrix[col-i-1][j], matrix[i][j]
		}
	}
}

// transpose by main diagonal
func transpose(matrix [][]int) {
	for i := 0; i < len(matrix); i++ {
		for j := i; j < len(matrix[0]); j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
}

func rotate(matrix [][]int) {
	transpose(matrix)
	mirrorX(matrix)
}
