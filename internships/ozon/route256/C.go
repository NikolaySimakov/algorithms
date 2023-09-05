package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	rand.Seed(time.Now().Unix())
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	n, _ := strconv.Atoi(scanner.Text())
	var res [][]int

	for i := 0; i < n; i++ {
		res = append(res, FindRange(scanner))
	}

	for _, arr := range res {
		for _, v := range arr {
			fmt.Println(v)
		}
		fmt.Println("")
	}
}

func FindRange(scanner *bufio.Scanner) []int {

	var res []int
	arr := makeRange(15, 30)
	scanner.Scan()
	m, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < m; i++ {
		scanner.Scan()
		line := scanner.Text()
		k, _ := strconv.Atoi(line[3:])
		arr = filter(arr, k, string(line[0]) == ">")
		if len(arr) == 0 {
			res = append(res, -1)
		} else {
			res = append(res, arr[rand.Intn(len(arr))])
		}
	}

	return res
}

func makeRange(min, max int) []int {
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func filter(nums []int, val int, dir bool) []int {
	var res []int
	for _, v := range nums {
		if dir == true {
			if v >= val {
				res = append(res, v)
			}
		} else {
			if v <= val {
				res = append(res, v)
			}
		}
	}

	return res
}
