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

func split(s string) []string {
	var res []string = []string{}

	var i int = 0
	var size int = len(s)

	for {

		if s[i] == byte(' ') {
			res = append(res, s[:i])
			s = s[i+1:]
		}

		i++

		if i == size {
			return append(res, s)
		}
	}

}

func reverseWords(s string) string {
	sArray := split(s)
	r := ""

	for i, v := range sArray {
		reverseString([]byte(v))

		fmt.Println(v)

		r += v
		if i != len(sArray)-1 {
			r += " "
		}
	}

	return r
}

func main() {
	s := "Let's take LeetCode contest"
	fmt.Println(reverseWords(s))
}
