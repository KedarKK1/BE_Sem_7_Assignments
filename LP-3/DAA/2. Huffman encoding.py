# Write a program to implement Huffman Encoding using a greedy strategy.

import collections, heapq

# d - tree direction (0/1)
Node = collections.namedtuple('Node',['d','freq','lchild','rchild'])

def print_codes(root, code):
    if root is not None:
        if(root.d != "$"):
            print(f"{root.d}: {code}")
        print_codes(root.lchild, code + "0") 
        print_codes(root.rchild, code + "1")

def HuffmanCodes(data, frequency):
    min_heap = []
    for i in range(len(data)):
        heapq.heappush(min_heap, Node(data[i], frequency[i], None, None))
    while(len(min_heap) > 1):
        lchild = heapq.heappop(min_heap)
        rchild = heapq.heappop(min_heap)
        top = Node("$", lchild.freq + rchild.freq, lchild, rchild)
        heapq.heappush(min_heap, top)
    print("Huffman Code: ")
    print_codes(min_heap[0], "") 

def main():
    # # characters for huffman tree & # frequency of characters
    arr, freq = ['a', 'b', 'c', 'd', 'e', 'f'], [5, 9, 12, 13, 16, 45]

    HuffmanCodes(arr, freq)

main()