package main

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	if num1 == "1" {
		return num2
	}
	if num2 == "1" {
		return num1
	}

	// for all numbers: len(num1*num2) = len(num1)+len(num2)-1 || len(num1)+len(num2)
	res := make([]byte, len(num1)+len(num2))

	for i := len(num1) - 1; i >= 0; i-- {
		for j := len(num2) - 1; j >= 0; j-- {
			res[i+j+1] += (num1[i] - '0') * (num2[j] - '0') // multiply char codes of (number1 - '0') and (number2 - '0'), char codes go sequentially
			res[i+j] += res[i+j+1] / 10                     // getting decimal place value
			res[i+j+1] %= 10                                // getting mod
		}
	}

	if res[0] == 0 {
		res = res[1:]
	}

	for i := range res {
		res[i] += '0'
	}

	return string(res)
}
