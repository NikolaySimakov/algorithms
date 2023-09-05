package main

import (
	"fmt"
	"strings"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)

	ipSet := make(map[string]bool)
	for i := 0; i < n; i++ {
		var ip string
		fmt.Scan(&ip)
		ipSet[ip] = true
	}

	var filters []string

	for ip := range ipSet {
		parts := strings.Split(ip, ".")
		x, y := parts[2], parts[3]

		if x == "0" && y == "0" {
			filters = append(filters, parts[0]+"."+parts[1]+".0.0/16")
		} else if y == "0" {
			filters = append(filters, parts[0]+"."+parts[1]+"."+x+".0/24")
		} else {
			filters = append(filters, ip)
		}
	}

	fmt.Println(65536 - len(ipSet))
	fmt.Println(len(filters))
	for _, filter := range filters {
		fmt.Println(filter)
	}
}
