def lex(N, K, R, arr):
    n = N
    k = K
    r = R
    A2 = arr
    A = []
    m = 0

    while m != k - 1:

        if A2[m] < A2[m + 1]:
            A.append(A2[m])
            m += 1
        else:
            print("ERROR")
            A = []
            break

    if len(A) != 0:
        A.append(A2[m])

    if k == n:
        # print("k==n")
        m = 1
    else:
        # print("k!=n")
        m = k

    x = 1

    while m >= 1:

        # print("first:", x)
        x += 1
        print(A)

        r -= 1
        if r == 0:
            # print("break")
            break
        else:
            if A[k - 1] == n:
                # print("3")
                # m = k
                m -= 1
            else:
                m = k
                # m -= 1
            # print(k)
            if m >= 1:
                # print("in if")
                # print("k: ", k)
                # print("m: ", m)
                for i in range(k, m - 1, -1):
                    # print("123")
                    A[i - 1] = A[m - 1] + i - m + 1
                    # print("321")


# lex(5, 3, 5, [1, 2, 4])


### и вот тут второй (мой алгортим)
n = 5
k = 4
R = ["Київ", "Харків", "Днепр", "Никополь", "Борисполь"]
A2 = [1, 2, 3]
A = []

for i in range(1, k + 1):
    A.append(i)

if k == n:
    m = 1
else:
    m = k

while m >= 1:
    for i in range(len(A)):
        print(R[A[i] - 1])

    if A[k - 1] == n:
        m -= 1
    else:
        m = k

    if m >= 1:
        print("m: ", m)
        if m >= 1:
            for i in range(k, m - 1, -1):
                A[i - 1] = A[m - 1] + i - m + 1
    else:
        break
