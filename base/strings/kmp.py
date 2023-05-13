# https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9A%D0%BD%D1%83%D1%82%D0%B0_%E2%80%94_%D0%9C%D0%BE%D1%80%D1%80%D0%B8%D1%81%D0%B0_%E2%80%94_%D0%9F%D1%80%D0%B0%D1%82%D1%82%D0%B0
# https://habr.com/ru/articles/191454/

class KMP:

    def trivial(self, haystack, needle):
        index = -1
        for i in range(len(haystack)-len(needle)+1):
            success = True
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    success = False
                    break
            if success:
                index = i
                break

        return index

    def prefix(self, s):
        v = [0]*len(s)
        for i in range(1, len(s)):
            k = v[i-1]
            while k > 0 and s[k] != s[i]:
                k = v[k-1]
            if s[k] == s[i]:
                k = k + 1
            v[i] = k
        return v

    def kmp(self, s, t):
        index = -1
        f = self.prefix(s)
        k = 0
        for i in range(len(t)):
            while k > 0 and s[k] != t[i]:
                k = f[k-1]
            if s[k] == t[i]:
                k = k + 1
            if k == len(s):
                index = i - len(s) + 1
                break
        return index


if __name__ == '__main__':

    haystack = 'some string'
    needle = 'str'

    search = KMP()
    trivial_search = search.trivial(haystack, needle)
    print(trivial_search)

    kmp = search.kmp(needle, haystack)
    print(kmp)
