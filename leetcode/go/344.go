package main

import "fmt"

func reverseString(s []byte) {

	var i int = 0
	var j int = len(s) - 1

	for {
		s[i], s[j] = s[j], s[i]

		i++
		j--

		if i >= j {
			break
		}
	}
}

func main() {
	str := []byte{'h', 'e', 'l', 'l', 'o'}
	reverseString(str)
	fmt.Println(str)
}
