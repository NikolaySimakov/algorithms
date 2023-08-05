n = int(input())
s = input()


def check(substr, string):
    i = len(string)
    while i != 0:
        if len(string) >= len(substr):
            if '#' in string[:len(substr)]:
                for i in range(len(substr)):
                    if string[i] == '#':
                        string = string[:i] + substr[i] + string[i+1:]
            elif '#' in substr:
                for i in range(len(substr)):
                    if substr[i] == '#':
                        substr = substr[:i] + string[i] + substr[i+1:]

            if string[:len(substr)] == substr:
                string = string[len(substr):]
                i -= len(substr)
            else:
                return False
        else:

            if '#' in string:
                for i in range(len(string)):
                    if string[i] == '#':
                        string = string[:i] + substr[i] + string[i:]
            elif '#' in substr[:len(string)]:
                for i in range(len(string)):
                    if string[i] == '#':
                        substr = substr[:i] + string[i] + substr[i:]

            return substr[:len(string)] == string

    return True


for i in range(1, n-1):
    if check(s[:i], s[i:]):
        print(s[:i])
        break
