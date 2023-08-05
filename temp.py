
def minStartValue(nums) -> int:
    start_value = 1

    while True:
        step_sum = start_value
        for num in nums:
            step_sum += num
            if step_sum < 1:
                start_value += 1
                break
        else:
            return start_value


print(minStartValue([-3,2,-3,4,2]))
