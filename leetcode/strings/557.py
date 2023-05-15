s = "Let's take LeetCode contest"

a = ' '.join(list(map(''.join, map(list, map(reversed, s.split())))))
print(a)
