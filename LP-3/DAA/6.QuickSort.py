import random, time

def partition(l, r, a):
    p = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= p:
            i = i + 1
            (a[i], a[j]) = (a[j], a[i])
    (a[i + 1], a[r]) = (a[r], a[i + 1])
    return i + 1

def partition_rand(l, r, a):
    pivot = random.randrange(l, r)
    a[r], a[pivot] = a[pivot], a[r]
    return partition(l, r, a)

def qsort(l, r, a):
    if l < r:
        pi = partition_rand(l, r, a)
        qsort(l, pi - 1, a)
        qsort(pi + 1, r, a)
    print("qsort ", a)

# def main(a, left, n):
#     # n = int(input("Enter no of elements:"))
#     # a = []
#     # for i in range(n):
#     #     b = int(input("Enter element:"))
#     #     a.append(b)
#     l = left
#     r = n - 1
#     qsort(l, r, a)
#     # for i in range(n):
#     #     print(a[i])
#     print(a)

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(low, high, arr)

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)
    print("randomized_quicksort ", arr)

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = [random.randint(1, 1000) for _ in range(n)]
    print(arr)

    # Analyze deterministic Quick Sort
    start_time = time.time()
    qsort(0, n - 1, arr.copy())
    end_time = time.time()
    print(f"Deterministic Quick Sort took {end_time - start_time:.6f} seconds")

    # Analyze randomized Quick Sort
    start_time2 = time.time()
    randomized_quicksort(arr.copy(), 0, n - 1)
    end_time2 = time.time()
    print(f"Randomized Quick Sort took {end_time2 - start_time2:.6f} seconds")

