package main

import (
	"fmt"
)

func firstUniqChar(s string) int {

	var proxy []byte = []byte(s)
	var arr []int = []int{}

	for i, v := range proxy {

		flag := false
		indx := 0

		for idx, a := range arr {
			if s[a] == v {
				flag = true
				indx = idx
			}
		}

		if flag {
			arr = append(arr[:indx], arr[indx+1:]...)
		} else {
			arr = append(arr, i)
		}
	}

	if len(arr) == 0 {
		return -1
	} else {
		return arr[0]
	}
}

func main() {
	s := "loveleetcode"
	fmt.Println(firstUniqChar(s))
}
