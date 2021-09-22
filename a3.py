


N = int(input())
M = int(input())


def gelukkig(X):
    seen_before = [X]
    num = X
    while True:
        num = sum([int(i)**2 for i in list(str(num))])
        if num == 1:
            return (True, seen_before)
        if num in seen_before:
            return (False, seen_before)
        else:
            seen_before.append(num)


nums = 0
for i in range(N, M+1):
    gel_data = gelukkig(i)
    if gel_data[0]:
        nums += 1

print(nums)