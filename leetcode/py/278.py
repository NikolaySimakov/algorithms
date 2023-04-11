
nums = [-1, 0, 3, 5, 9, 12]
target = 9

index = 0

while True:
    l1 = len(nums)//2

    if nums[l1] > target:
        nums = nums[:l1]
        if len(nums) == 1:
            print(index)
            break

    elif nums[l1] <= target:
        index += l1
        nums = nums[l1:]
        if len(nums) == 1:
            print(index)
            break
