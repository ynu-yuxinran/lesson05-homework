def bubble_sort(nums):
    """冒泡排序：重复比较相邻元素，把较大的逐步“冒泡”到末尾。
    时间复杂度 O(n^2)，空间复杂度 O(1)，稳定排序。
    本实现不修改原数组，返回排好序的新列表。
    """
    arr = list(nums)            # 做副本，不改动原数组
    n = len(arr)
    for i in range(n - 1):      # 外层：共需 n-1 轮
        swapped = False
        for j in range(n - 1 - i):   # 内层：每轮把当前最大值冒到末尾
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:         # 本轮没有交换，说明已有序，提前退出
            break
    return arr


def binary_search(rates, target):
    """二分查找：在有序数组 rates 中查找 target。
    前提：rates 必须已按升序排好——不满足此前提，结果不可预测。
    返回 (下标, 比较次数)；找不到返回 (-1, 比较次数)。
    """
    low, high = 0, len(rates) - 1
    count = 0  # 记录比较次数
    while low <= high:
        mid = (low + high) // 2   # 中间档
        count += 1                # 第 1 次比较：是否相等
        if rates[mid] == target:
            return mid, count
        count += 1                # 第 2 次比较：判断大小方向
        if rates[mid] < target:
            low = mid + 1         # 目标在右半段
        else:
            high = mid - 1        # 目标在左半段
    return -1, count


def main():
    # ===== 测试一：1024 档有序利率表，查找 3.75% =====
    # 生成 0.01, 0.02, ..., 10.24 共 1024 个有序利率（升序）
    rates = [round(i * 0.01, 2) for i in range(1, 1025)]
    target = 3.75
    idx, count = binary_search(rates, target)
    print(f"【测试一】在 {len(rates)} 档利率表中查找 {target}%")
    print(f"  找到下标: {idx}，该档位利率: {rates[idx]}%，比较次数: {count}")

    # ===== 测试二：翻车实验 —— 故意用乱序数组跑二分查找 =====
    print()
    messy = [8, 3, 5, 1, 9, 2]          # 故意未排序
    target2 = 3
    print(f"【测试二·翻车实验】在乱序数组 {messy} 中查找 {target2}")
    print(f"  （{target2} 实际位于下标 1）")
    idx2, count2 = binary_search(messy, target2)
    print(f"  二分查找返回下标: {idx2}，比较次数: {count2}")
    if idx2 == -1 or messy[idx2] != target2:
        print(f"  → 翻车：元素明明存在，却返回 {idx2}！")
        print(f"    原因：数组无序，二分查找的前提不成立，搜索方向走错，错过了它。")
    else:
        print(f"  → 碰巧蒙对了，但这只是巧合，换个元素就翻车。")

    # 对比：先用冒泡排序排好，再二分查找
    sorted_messy = bubble_sort(messy)
    idx3, count3 = binary_search(sorted_messy, target2)
    print(f"  对比：先冒泡排序得 {sorted_messy}，再二分查找返回下标: {idx3}，比较次数: {count3}")


if __name__ == "__main__":
    main()