package main

import "fmt"

// n=1 -> 5
// n=2 -> 5 + 4 + 3 + 2 + 1 = (n+1)*n/2
// n=3 -> 5 + 4 + 3 + 2 + 1 + 4 + 3 + 2 + 1 + 3 + 2 + 1 + 2 + 1 + 1 = (1+1)*1/2 + (2+1)*2/2 + (3+1)*3/2 + (4+1)*4/2 + (5+1)*5/2

// math solution
func countVowelStringsMath(n int) int {
	var res int = 0

	for i := 1; i <= n+1; i++ {
		for j := 1; j <= i; j++ {
			res += (j + 1) * j / 2
		}
	}

	return res
}

// dynamic programming solution
func countVowelStringsDP(n int) int {

	if n == 1 {
		return 5
	}

	var dp = make(map[string]int)

	dp["a"], dp["e"], dp["i"], dp["o"], dp["u"] = 1, 1, 1, 1, 1

	for i := 2; i <= n; i++ {
		dp["o"]++
		dp["i"] += dp["o"]
		dp["e"] += dp["i"]
		dp["a"] += dp["e"]
	}

	return 1 + dp["a"] + dp["e"] + dp["i"] + dp["o"]
}

func main() {
	n := 33
	fmt.Println(countVowelStringsMath(n))
	fmt.Println(countVowelStringsDP(n))
}
