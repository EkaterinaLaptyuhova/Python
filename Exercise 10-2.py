def cumsum(t):
    cum_t = []
    i = 0
    while i < len(t):
        cum_t.append(sum(t[: i + 1]))
        i += 1

    print(cum_t)


cumsum([1,3,2,5,3])