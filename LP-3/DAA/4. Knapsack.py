import collections

Item = collections.namedtuple('Item', ['profit', 'weight'])

def Knapsack(arr, n, w):
    if(n == 0 or w == 0):
        return 0
    if(arr[n-1].weight <= w):
        return max(Knapsack(arr, n-1, w - arr[n-1].weight) + arr[n-1].profit ,
                    Knapsack(arr, n-1, w)                   
                   )
    else:
        return Knapsack(arr, n-1, w)

def main():
    # # characters for huffman tree & # frequency of characters
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    n = len(arr)
    print(Knapsack(arr, n, 50))

main()