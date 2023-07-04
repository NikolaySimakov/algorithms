n = int(input())
arr1 = [list(map(int, input().split())) for _ in range(3)]
m = int(input())
arr2 = [list(map(int, input().split())) for _ in range(3)]

res = [0]*m

salary = arr1[0]
s1 = set([i for i in range(n) if arr1[1][i] == 1]) # важно образование
s2 = set([i+1 for i in range(n) if arr1[2][i] != 0])

print(s1, s2)

for i in range(m):
    # con1 = arr2[0][i] >= salary[j]
    # con2 = arr2[1][i] == 1 if arr1[1][j] else True
    # con3 = arr2[2][i] in s2
    country1 = country2 = None
    my_salary = arr2[0][i]
    if arr2[1][i] == 1:
        a_countries = list(filter(lambda x: x in s1 and my_salary > salary[x], list(range(n))))
        if len(a_countries) > 0:
            country1 = a_countries[0]
    else:
        for s in range(n):
            if my_salary >= salary[s]:
                country1 = s
    
    if arr2[2][i] in s2:
        country2 = arr2[2][i]
        
    print(country1, country2)
        
    # if (con1 and con2) or con3:
    #     res[i] = j + 1
    #     break

print(*res)