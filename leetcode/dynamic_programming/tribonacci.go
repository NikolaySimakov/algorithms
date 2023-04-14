package main

import "fmt"

func tribonacci(n int) int {
	l := []int{0, 1, 1}

	for i := 3; i <= n; i++ {
		l = append(l, l[i-1]+l[i-2]+l[i-3])
	}

	return l[n]
}

func main() {
	n := 1
	fmt.Println(tribonacci(n))
}
