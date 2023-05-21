# def maximize_discount(n, m, k, prices, discounts, coupons):
#     # Calculate maximum discounts using dynamic programming
#     dp = [[0] * (k+1) for _ in range(n+1)]
#     for i in range(1, n+1):
#         for j in range(1, k+1):
#             if not discounts[i-1]:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 applicable_coupons = [c for c in discounts[i-1] if c <= m]
#                 if not applicable_coupons:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     max_discount = dp[i-1][j-1]
#                     for c in applicable_coupons:
#                         new_discount = prices[i-1] * coupons[c-1] // 100
#                         max_discount = max(
#                             max_discount, dp[i-1][j-1] + new_discount)
#                     dp[i][j] = max(max_discount, dp[i-1][j])
#     max_discount = dp[n][k]

#     # Backtrack to obtain list of coupons to apply
#     cart_coupons = []
#     i, j = n, k
#     while i > 0 and j > 0:
#         if dp[i][j] == dp[i-1][j]:
#             i -= 1
#         else:
#             applicable_coupons = [c for c in discounts[i-1] if c <= m]
#             if not applicable_coupons:
#                 i -= 1
#             else:
#                 max_discount = dp[i-1][j-1]
#                 best_coupon = None
#                 for c in applicable_coupons:
#                     new_discount = prices[i-1] * coupons[c-1] // 100
#                     if dp[i-1][j-1] + new_discount == dp[i][j]:
#                         best_coupon = c
#                         break
#                     elif dp[i-1][j-1] + new_discount > max_discount:
#                         max_discount = dp[i-1][j-1] + new_discount
#                         best_coupon = c
#                 if best_coupon is not None:
#                     cart_coupons.append(best_coupon)
#                     j -= 1
#                     i -= 1
#                     discount = prices[i-1] * coupons[```
