from threading import Thread

MAX, MAX_THREAD = 4, 4

FinalMatrix = [[0 for i in range(MAX)] for j in range(MAX)]

step_i = 0

# Function to multiply a row of matrix A  with entire matrix B to get a row of matrix C


def multi():
    global step_i, FinalMatrix
    i = step_i
    step_i += 1
    for j in range(MAX):
        for k in range(MAX):
            FinalMatrix[i][j] += (A[i][k] * B[k][j])


def normalMultiplication(a, b):
    ans = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for m in range(len(a)):
        for n in range(len(b[0])):
            for o in range(len(b)):
                ans[m][n] += (a[m][o] * b[o][n])
    print(ans)


if __name__ == "__main__":
    # A = [[5, 4, 3],
    #      [2, 4, 6],
    #      [4, 7, 9]]
    # B = [[3, 2, 4],
    #      [4, 3, 6],
    #      [2, 7, 5]]
    # [37, 43, 59]
    # [34, 58, 62]
    # [58, 92, 103]
    # normalMultiplication(A, B)

    A = [[3, 7, 3, 6],
         [9, 2, 0, 3],
         [0, 2, 1, 7],
         [2, 2, 7, 9]]
    B = [[6, 5, 5, 2],
         [1, 7, 9, 6],
         [6, 6, 8, 9],
         [0, 3, 5, 2]]
    # creating list of size MAX_THREAD
    thread = list(range(MAX_THREAD))
    for i in range(MAX_THREAD):
        thread[i] = Thread(target=multi)
        thread[i].start()

    # Waiting for all threads to finish
    for i in range(MAX_THREAD):
        thread[i].join()

    print(FinalMatrix)
    normalMultiplication(A, B)

    # A = [[7 2 6 8
    # 7 0 6 6
    # 6 1 7 5
    # 3 7 7 2]]
    # B = 3 5 3 6
    # 5 7 5 8
    # 8 9 4 9
    # 6 5 7 2
    # Multiplication of A and B
    # 127 143 111 128
    # 105 119 87 108
    # 109 125 86 117
    # 112 137 86 141
# main()
