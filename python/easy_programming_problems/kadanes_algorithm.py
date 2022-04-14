def kadane(nums):
    max_so_far = nums[0]
    current_max = nums[0]
    for num in nums:
        max_so_far = max([max_so_far + num, num])
        current_max = max(current_max, max_so_far)
    return current_max

if __name__ == "__main__":
    print(kadane([-2, -3, 4, -1, -2, 1, 5, -3]))

