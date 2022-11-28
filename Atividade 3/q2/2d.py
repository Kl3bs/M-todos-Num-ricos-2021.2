def neville(x_values, y_values, x):

    n = len(x_values)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = y_values[i]
            else:
                p[i] = ((x-x_values[i+k])*p[i] +
                        (x_values[i]-x)*p[i+1]) / \
                    (x_values[i]-x_values[i+k])
    return p[0]


x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

print(neville(x, y, 60))
