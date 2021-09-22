
N = int(input())
B = format(N, "b")
A = B[::-1]
A_zeros = A.split("1")
M = len(A_zeros[0])
P = int(A, 2)
print(M)
print(P)
