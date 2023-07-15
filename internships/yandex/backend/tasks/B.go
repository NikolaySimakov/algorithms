package main

import "fmt"

func passengersInPlane() ([]string, []string) {

}

func main() {

	var n int
	var m int

	fmt.Scan(&n)

	arr := make([]string, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&m)

	res := passengersInPlane()
	fmt.Println(res)
}
