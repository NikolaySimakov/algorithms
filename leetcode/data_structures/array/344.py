from typing import List


def reverseString(s: List[str]) -> None:

    i = 0
    j = len(s)-1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


a = ["h", "e", "l", "l", "o"]
reverseString(a)
print(a)
