# ===== 1. 两数之和 =====
# https://leetcode.cn/problems/two-sum/
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# ===== 704. 二分查找 =====
# https://leetcode.cn/problems/binary-search/
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ===== 344. 反转字符串 =====
# https://leetcode.cn/problems/reverse-string/
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 测试
if __name__ == "__main__":
    # 两数之和
    print("两数之和:", twoSum([2,7,11,15], 9))  # [0, 1]
    # 二分查找
    print("二分查找:", search([-1,0,3,5,9,12], 9))  # 4
    # 反转字符串
    s = ["h","e","l","l","o"]
    reverseString(s)
    print("反转字符串:", s)  # ["o","l","l","e","h"]
