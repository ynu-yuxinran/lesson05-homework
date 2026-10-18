# -*- coding: utf-8 -*-
# 等额本息月供计算器 + 二分查找最接近目标月供的利率

PRINCIPAL = 1000000      # 贷款本金：100万元
LOAN_YEARS = 30          # 贷款年限：30年
N = LOAN_YEARS * 12      # 还款月数
TARGET = 5000            # 目标月供


def monthly_payment(P, annual_rate, n):
    """等额本息月供 M = P*r*(1+r)^n / ((1+r)^n - 1)"""
    r = annual_rate / 12
    if r == 0:
        return P / n
    p = (1 + r) ** n
    return P * r * p / (p - 1)


def main():
    # 生成100个升序利率：3.00% ~ 7.95%，步长0.05%
    rates = [round(0.03 + i * 0.0005, 6) for i in range(100)]

    print("共生成 %d 个利率，范围 %.2f%% ~ %.2f%%" % (len(rates), rates[0]*100, rates[-1]*100), flush=True)
    print("本金 %d 元，期限 %d 年，目标月供 %d 元" % (PRINCIPAL, LOAN_YEARS, TARGET), flush=True)
    print("-" * 55, flush=True)

    # 二分查找：月供随利率单调递增
    lo, hi = 0, len(rates) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        m = monthly_payment(PRINCIPAL, rates[mid], N)
        print("  mid=%d  利率=%.2f%%  月供=%.2f 元" % (mid, rates[mid]*100, m), flush=True)
        if abs(m - TARGET) < 0.01:
            lo = mid
            break
        elif m < TARGET:
            lo = mid + 1
        else:
            hi = mid - 1

    # 在 hi 和 lo 两个相邻位置中选月供更接近目标的
    cand = set()
    if 0 <= hi < len(rates):
        cand.add(hi)
    if 0 <= lo < len(rates):
        cand.add(lo)
    best = min(cand, key=lambda i: abs(monthly_payment(PRINCIPAL, rates[i], N) - TARGET))

    print("-" * 55, flush=True)
    print("最接近目标月供的利率: %.2f%%" % (rates[best] * 100), flush=True)
    print("对应月供: %.2f 元" % monthly_payment(PRINCIPAL, rates[best], N), flush=True)


if __name__ == "__main__":
    main()