def num_of_delitel(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    return count


print(num_of_delitel(10))
