def merge_sort(nums, depth=0):
    """合并排序:分治三步的完整样板"""
    # 打印当前递归调用深度
    print(f"[递归深度 {depth}] 处理数组: {nums}")

    # 基准情形：长度0或1的数组天然有序
    if len(nums) <= 1:
        return nums

    # ---分解---(Divide): 从中间切成两半 ---
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # ---解决---(Conquer): 递归排序两个小段 ---
    left_sorted = merge_sort(left, depth + 1)
    right_sorted = merge_sort(right, depth + 1)

    # ---合并---(Combine): 将两个有序小段合并成一个有序段 ---
    return merge(left_sorted, right_sorted)


def merge(a, b):
    """双指针合并两个有序数组"""
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # 取较小者入结果
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    # 残段必有序，直接接上
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def main():
    """主函数：测试合并排序"""
    arr = [8, 3, 5, 1, 9, 2]
    print(f"原始数组: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"排序结果: {sorted_arr}")


if __name__ == "__main__":
    main()


