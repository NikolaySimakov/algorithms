def isSubsequence(s: str, t: str) -> bool:
    j = 0

    for i in t:
        if j == len(s):
            return True

        if i == s[j]:
            j += 1

    return j == len(s)


print(isSubsequence("abc", "ahbgdc"))
