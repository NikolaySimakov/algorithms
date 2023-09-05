package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var sums []int
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < n; i++ {
		scanner.Scan()
		sums = append(sums, Sum(scanner.Text()))
	}

	for _, v := range sums {
		fmt.Println(v)
	}
}

func Sum(l string) int {
	var a, b int
	fmt.Sscanf(l, "%d %d", &a, &b)
	return a + b
}
