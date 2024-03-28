def series_sum(n):
    sum = 1
    if n == 0:
        sum = 0.00
        return format(sum, ".2f")
    elif n > 1:
        for i in range(1, n):
           sum += 1/(1 + i * 3)
    return format(sum, ".2f")