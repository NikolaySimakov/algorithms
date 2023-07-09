package main

func canJump(nums []int) bool {

	n := len(nums)
	dp := make([]bool, n-1)
	dp = append(dp, true)

	for i := n - 2; i >= 0; i-- {
		for j := i; j <= i+nums[i]; j++ {
			if dp[j] {
				dp[i] = true
				break
			}
		}
	}

	return dp[0]
}
