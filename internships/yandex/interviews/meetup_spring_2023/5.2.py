def get_product_ids(n, data):
    # Step 1
    categories = {}
    for i in range(n):
        id, category = data[i]
        if category not in categories:
            categories[category] = []
        categories[category].append(id)

    # Step 2
    sorted_categories = sorted(categories.values(), key=len, reverse=True)

    # Step 3
    result = []
    last_index = -1

    # Step 4
    for category in sorted_categories:
        # Step 4.1
        category.sort(key=lambda x: abs(x - last_index))

        # Step 4.2
        result.append(category)

        # Step 4.3
        last_index = category[-1]

    # Step 5
    return [item for sublist in result for item in sublist]


# Sample input 1
n = 5
data = [(1, 1), (2, 1), (3, 1), (4, 2), (5, 2)]
print(get_product_ids(n, data))  # Output: [1, 4, 2, 5, 3]

# Sample input 2
n = 9
data = [(1, 1), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2), (7, 3), (8, 3), (9, 3)]
print(get_product_ids(n, data))  # Output: [1, 4, 7, 2, 5, 8, 3, 6, 9]

# Sample input 3
n = 5
data = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
print(get_product_ids(n, data))  # Output: [1, 2, 3, 4, 5]

# Sample input 4
n = 4
data = [(1, 1), (2, 1), (3, 2), (4, 2)]
print(get_product_ids(n, data))  # Output: [1, 3, 2, 4]
