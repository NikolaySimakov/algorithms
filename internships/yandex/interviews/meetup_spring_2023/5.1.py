def sort_items(n, items):
    # Group items by category
    categories = {}
    for i, c in items:
        if c not in categories:
            categories[c] = []
        categories[c].append(i)

    # Sort items within each category
    for c in categories:
        categories[c].sort()

    # Initialize result list
    result = []

    # Process categories until all items are sorted
    while categories:
        # Find category with lowest remaining items
        min_category = min(categories, key=lambda c: len(categories[c]))

        # Take first item from category and add to result list
        item = categories[min_category].pop(0)
        result.append(item)

        # Remove category if no items remaining
        if not categories[min_category]:
            del categories[min_category]

    return result


n = int(input())
pairs = []

for i in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

print(sort_items(n, pairs))
