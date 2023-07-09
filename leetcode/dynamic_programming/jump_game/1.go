package main

/*
Solution: we run from n-2 to 0 and for each next value in the jump range
we check whether it is possible to get there.
And so on up to position 0.
*/

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
