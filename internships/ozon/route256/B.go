package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	var prices []int

	for i := 0; i < n; i++ {
		scanner.Scan()
		m, _ := strconv.Atoi(scanner.Text())

		scanner.Scan()
		numsStr := strings.Split(scanner.Text(), " ")
		nums := make([]int, 0, len(numsStr))
		for _, numStr := range numsStr {
			v, _ := strconv.Atoi(numStr)
			nums = append(nums, v)
		}
		prices = append(prices, Price(m, nums))
	}

	for _, price := range prices {
		fmt.Println(price)
	}
}

func Price(n int, nums []int) int {

	var price int
	counter := make(map[int]int)

	for i := 0; i < n; i++ {
		counter[nums[i]] += 1
	}

	for p, ct := range counter {
		price += p * (ct - int(ct/3))
	}

	return price
}
