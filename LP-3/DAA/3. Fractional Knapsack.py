import collections

Item = collections.namedtuple('Item', ['profit', 'weight'])

def FractionalKnapsack2(arr, n, W):
    summ, tot = W, 0
    for i in range(n):
        summ -= arr[i].weight
        if(summ >= 0):
            tot += arr[i].profit
        elif(arr[i].weight >= summ):
            summ += arr[i].weight
            # print("Sum ", summ)
            tot += arr[i].profit * summ // arr[i].weight
            summ -= arr[i].weight
            # print("Tota ", tot)
        # print("tot ", tot)
    # print("Total ", tot)
    return tot

def FractionalKnapsack(arr, W):
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
    # print(arr)
    ans = 0.0
    for i in arr:
        if(i.weight <= W):
            W -= i.weight
            ans += i.profit
        else:
            ans += i.profit * W // i.weight
            break
    return ans


def main():
    # # characters for huffman tree & # frequency of characters
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    print(FractionalKnapsack(arr, 50))
    print(FractionalKnapsack2(arr, len(arr), 50))


main()
