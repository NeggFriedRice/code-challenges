def get_sum(a,b):
    if a>b : a,b = b,a
    return sum(range(a,b+1))

# Failed
    
print(get_sum(0, -1))