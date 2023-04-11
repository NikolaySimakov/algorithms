package main

import "fmt"

func fib(n int) int {

	var values = []int{0, 1, 1}

	for i := 3; i <= n; i++ {
		values = append(values, values[i-1]+values[i-2])
	}

	return values[n]
}

func main() {
	n := 11
	res := fib(n)
	fmt.Println(res)
}
