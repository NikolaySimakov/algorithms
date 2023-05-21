n = int(input())
pairs = []

for i in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))


def get_farthest_product_ids(n, products):
    # Create a dictionary with categories as keys and lists of product ids as values
    categories = {}
    for i in range(n):
        pid, cat = products[i]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(pid)

    # Sort the lists of product ids in the dictionary by length
    for cat in categories:
        categories[cat].sort(key=len, reverse=True)

    # Create an empty result array
    result = []

    # Loop through the lists of product ids in the dictionary
    for cat in categories:
        ids = categories[cat]
        if len(ids) == 1:
            result.append(ids[0])
        else:
            # Add the first element of each list to the result array
            for i in range(len(ids)):
                if i == 0:
                    result.append(ids[i])
                else:
                    # Loop through the remaining elements of each list and add them to the result array,
                    # ensuring that they are placed as far apart as possible from the previously added elements
                    j = i
                    while j < len(ids):
                        if ids[j] not in result:
                            result.append(ids[j])
                            break
                        j += 1

    # Return the result array
    return result


print(get_farthest_product_ids(n, pairs))

# arr = []

# while len(arr) < n:

#     dist = 0
#     v = 0

#     for i in p.keys():
#         if p[i] in d.keys():
#             if (len(arr) - d[p[i]]) > dist:
#                 dist = len(arr) - d[p[i]]
#                 v = i
#         else:
#             v = i
#             break

#     d[p[v]] = len(arr)
#     del p[v]
#     arr.append(v)


# print(*arr)

# n = int(input())
# products = []
# for i in range(n):
#     id, category = map(int, input().split())
#     products.append({'id': id, 'category': category})

# sorted_products = sorted(products, key=lambda p: p['category'])

# result = []
# for p in sorted_products:
#     result.append(p['id'])

# print(result)
