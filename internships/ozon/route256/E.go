package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	vals := makeRange(0, m)
	var res []int

	for _, p := range arr {
		v, i := bs(vals, p)
		if v > p {
			vals = remove(vals, i)
			res = append(res, v)
		}
	}

	if len(res) == n {
		var strNums []string
		for _, num := range res {
			strNums = append(strNums, strconv.Itoa(num))
		}

		result := strings.Join(strNums, " ")
		fmt.Println(result)
	} else {
		fmt.Println(-1)
	}
}

func makeRange(min, max int) []int {
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func remove(slice []int, s int) []int {
	return append(slice[:s], slice[s+1:]...)
}

func bs(arr []int, target int) (int, int) {
	l, r := 0, len(arr)-1
	for l < r {
		mid := l + (r-l)/2
		if arr[mid] <= target {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}

	return arr[l], l
}
