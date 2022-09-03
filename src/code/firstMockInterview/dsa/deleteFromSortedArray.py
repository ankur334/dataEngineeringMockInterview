
def delete_from_array(nums):
    i, j = 0, 1
    while i < len(nums) - 1:
        if nums[i + 1] != nums[i]:
            nums[j] = nums[i + 1]
            j = j + 1
        i = i + 1

    return nums[:j]


if __name__ == '__main__':
    result = delete_from_array([1, 1, 2])
    print(result)