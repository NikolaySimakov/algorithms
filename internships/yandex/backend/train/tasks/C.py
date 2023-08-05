def distance(k, a, n):
    a_sorted = sorted(a)
    s = sum(a_sorted[1:k+1]) - k * a_sorted[0]
    answer = {a_sorted[0]:s}
    left = 0    # количество чисел слева от исходного числа в отсортированном массиве, которые ближе всего к нему
    right = k   # количество чисел справа
 
    for i in range(1, n):
        left += 1
        right -= 1
        dif = a_sorted[i] - a_sorted[i-1]   # разница прошлого числа и нынешнего (a_sorted[i] и a_sorted[i-1])
        s = s - dif*right + dif*(left-1)    # -1 тк разница между a_sorted[i] и a_sorted[i-1] осталось та же
        while right + i + 1 < n:
            l = a_sorted[i]-a_sorted[i-left]
            r = a_sorted[i+right+1] - a_sorted[i]
            if l > r: # если расстояние до левого больше, чем до правого, то двигаем окно k вправо
                right += 1
                left -= 1
                s -= (l-r) # и пересчитываем сумму
            else:
                break
        answer[a_sorted[i]] = s
 
    for num in a:
        print(answer[num], end=' ')
 
 
if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    distance(k, a, n)