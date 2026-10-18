import timeit
import random

# ============================================================
# 本次对比的三种排序实现
# 说明：bubble_sort / merge_sort 均来自本目录已写好的实现；
#       merge_sort 去掉了"递归深度打印"，避免 print 的 I/O 开销干扰计时公平性，
#       算法本体（分解/解决/合并）与 merge_sort..py 完全一致。
# ============================================================

def bubble_sort(nums):
    """冒泡排序：不修改原数组，返回新列表。"""
    arr = list(nums)
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge(a, b):
    """双指针合并两个有序数组。"""
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def merge_sort(nums):
    """合并排序：分治三步，返回新列表。"""
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

# ============================================================
# 性能测试
# ============================================================

NS = [1000, 2000, 4000, 8000]   # 测试规模
REPEAT = 3                       # 每个规模跑 3 次取平均

def bench_one(func, arr):
    """对单个排序函数跑 REPEAT 次，每次都用 arr[:] 新鲜副本，返回平均耗时（秒）。"""
    times = timeit.repeat(
        lambda: func(arr[:]),     # 关键：每次都复制副本，避免原数组被改
        number=1,
        repeat=REPEAT,
    )
    return sum(times) / len(times)

def main():
    print("性能测试开始，正在运行，请稍候...", flush=True)
    # 表头
    header = f"{'n':>8} | {'冒泡排序(s)':>14} | {'归并排序(s)':>14} | {'sorted(s)':>12} | {'冒泡/归并(倍)':>14}"
    print(header, flush=True)
    print("-" * len(header), flush=True)

    for n in NS:
        # 生成一个随机数组，三种排序共用同一份原始数据，保证公平
        arr = [random.randint(1, 10000) for _ in range(n)]

        t_bubble = bench_one(bubble_sort, arr)
        t_merge = bench_one(merge_sort, arr)
        t_sorted = bench_one(sorted, arr)

        # 冒泡比归并慢多少倍（>1 表示冒泡更慢；理论上 n 翻倍时该比值约翻倍，因为 O(n^2)/O(n log n)）
        ratio = t_bubble / t_merge

        print(f"{n:>8} | {t_bubble:>14.6f} | {t_merge:>14.6f} | {t_sorted:>12.6f} | {ratio:>14.2f}", flush=True)

    print(flush=True)
    print("说明：'冒泡/归并(倍)' = 冒泡耗时 / 归并耗时，值越大说明冒泡越慢。", flush=True)
    print("      理论上当 n 翻倍时，该比值大约也翻倍（O(n^2) 对比 O(n log n)）。", flush=True)

if __name__ == "__main__":
    main()