# LIS Largest Increasing Subsequence
# 导弹问题

if __name__ == "__main__":
    _ = input()
    s = input()
    s = [int(x) for x in s.split(' ')]
    r = [0]*len(s)                      # r 保存当前节点的最长递增子序列数
    for i in range(len(s)):
        tmax = 1
        for j in range(i+1):            # i 前面的所有点
            if s[j] >= s[i]:            # 如果 s[j] >= s[i]
                tmax = max(tmax, r[j]+1)# 那么更新最大值： tmax 为 tmax 和 r[j] 中大的数
        r[i] = tmax                     # r[i] := tmax
    print(max(r))

