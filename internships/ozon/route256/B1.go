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
	s := strings.Split(scanner.Text(), "")
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < n; i++ {
		scanner.Scan()
		inpArr := strings.Split(scanner.Text(), " ")
		startStr, endStr, sub := inpArr[0], inpArr[1], strings.Split(inpArr[2], "")
		start, _ := strconv.Atoi(startStr)
		end, _ := strconv.Atoi(endStr)

		for j := start - 1; j < end; j++ {
			s[j] = sub[j-start+1]
		}
	}

	fmt.Println(strings.Join(s, ""))

}
