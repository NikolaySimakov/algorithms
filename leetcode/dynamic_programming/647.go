package main

func countSubstrings(s string) int {
    n := len(s)
    dp := make([][]bool, n)
    count := 0

    for i := range dp {
        dp[i] = make([]bool, n)
    }

    for i := n - 1; i >= 0; i-- {
        dp[i][i] = true
        count++

        if i+1 < n {
			dp[i][i+1] = s[i] == s[i+1]
            if s[i] == s[i+1] {
                count++
            }
		}

        for j := i+2; j < n; j++ {
            eq := dp[i+1][j-1] && s[i] == s[j]
            dp[i][j] = eq
            if eq {
                count++
            }
        }
    }

    return count
}