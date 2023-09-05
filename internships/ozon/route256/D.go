package main

import (
	"fmt"
)

func main() {
	var k int
	fmt.Scan(&k)

	reliefs := make([][][]byte, k)
	for i := 0; i < k; i++ {
		var n, m int
		fmt.Scan(&n, &m)

		relief := make([][]byte, n)
		for j := 0; j < n; j++ {
			row := make([]byte, m)
			for k := 0; k < m; k++ {
				fmt.Scanf("%c", &row[k])
			}
			relief[j] = row
		}
		reliefs[i] = relief
	}

	n, m := len(reliefs[0]), len(reliefs[0][0])
	result := make([][]byte, n)
	for i := 0; i < n; i++ {
		result[i] = make([]byte, m)
		for j := 0; j < m; j++ {
			result[i][j] = '.'
		}
	}

	for j := 0; j < m; j++ {
		for i := n - 1; i >= 0; i-- {
			if reliefs[0][i][j] == '/' {
				for k := i; k >= 0; k-- {
					result[k][j] = 'X'
				}
				break
			} else if reliefs[0][i][j] == '\\' {
				for k := i; k >= 0; k-- {
					result[k][j] = 'X'
				}
				break
			} else if reliefs[0][i][j] == 'X' {
				break
			}
		}
	}

	for i := 0; i < n; i++ {
		fmt.Println(string(result[i]))
	}
}
