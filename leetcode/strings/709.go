package main

import "fmt"

// to lower case
func toLowerCase(s string) string {
	s_bytes := []byte(s)

	for i, v := range s_bytes {
		if v >= 65 && v <= 90 {
			s_bytes[i] = v + 32
		}
	}

	return string(s_bytes)
}

func main() {

	var s string
	var res string

	// Example 1
	s = "Hello"
	res = toLowerCase(s)
	fmt.Println(res)

	// Example 2
	s = "LOVELY"
	res = toLowerCase(s)
	fmt.Println(res)
}
