import numpy as np

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    res = np.zeros((n+1, m+1), 'int')
    res[0] = range(m+1)
    res[:,0] = range(n+1)

    for i in range(m):
        for j in range(n):
            cost = 0 if s1[i] == s2[j] else 1
            res[j+1, i+1] = min(res[j, i] + cost,
                                res[j+1, i] + 1,
                                res[j, i+1] +1)

    print(res)
    # 解的回溯
    s1_aligned = ""
    s2_aligned = ""
    i, j = m, n
    while (i>0) or (j>0):
        cost = 0 if s1[i-1] == s2[j-1] else 1
        if (res[j, i] == res[j-1, i-1] + cost):
            # \
            s1_aligned += s1[i-1]
            s2_aligned += s2[j-1]
            i -= 1
            j -= 1
        elif (res[j, i] == res[j, i-1] + 1):
            # -
            s1_aligned += s1[i-1]
            s2_aligned += "*"
            i -= 1
        else:
            # |
            s1_aligned += "*"
            s2_aligned += s2[j-1]
            j -= 1
    print(s1_aligned[::-1])
    print(s2_aligned[::-1])

if __name__ == "__main__":
    edit_distance("intention","execution")
