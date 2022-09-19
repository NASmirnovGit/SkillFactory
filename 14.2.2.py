def adder(*nums):
    p = 1
    for n in nums:
        p *= n
    return p


print(adder(1, 2, 4, 5))
