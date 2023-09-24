#include <bits/stdc++.h>;
using namespace std;

struct MinHeapNode
{
    char d;
    unsigned frequency;
    MinHeapNode *lChild, *rChild;

    MinHeapNode(char d, unsigned frequency)
    {
        lChild = rChild = NULL;
        this-&gt;d = d;
        this-&gt;frequency = frequency;
    }
};

//function to compare
struct compare
{
    bool operator()(MinHeapNode *l, MinHeapNode *r)
    {
        return (l-&gt;frequency &gt; r-&gt;frequency);
    }
};

void printCodes(struct MinHeapNode *root, string str)
{
    if (!root)
        return;

    if (root-&gt;d != &#39;$&#39;)
        cout &lt;&lt; root-&gt;d &lt;&lt; &quot;: &quot; &lt;&lt; str &lt;&lt; &quot;\n&quot;;

        printCodes(root-&gt;lChild, str + &quot;0&quot;);
        printCodes(root-&gt;rChild, str + &quot;1&quot;);
}

void showpq(
        priority_queue&lt;MinHeapNode *, vector&lt;MinHeapNode *&gt;, compare &gt; g)
    {
        while (!g.empty()) {
            cout &lt;&lt; &#39; &#39; &lt;&lt; g.top()-&gt;d;
            g.pop();
    }
        cout<<"\n";
    }

void HuffmanCodes(char d[], int frequency[], int size)
    {
        struct MinHeapNode *lChild, *rChild, *top;

        priority_queue&lt;MinHeapNode *, vector&lt;MinHeapNode *&gt;, compare&gt; minHeap;

        for (int i = 0; i &lt; size; ++i)
            minHeap.push(new MinHeapNode(d[i], frequency[i]));

        while (minHeap.size() != 1)
        {
            lChild = minHeap.top();
            minHeap.pop();

            rChild = minHeap.top();
            minHeap.pop();

            top = new MinHeapNode(&#39;$&#39;, lChild-&gt;frequency + rChild-&gt;frequency);

            top-&gt;lChild = lChild;
            top-&gt;rChild = rChild;

            minHeap.push(top);

        }
        printCodes(minHeap.top(), &quot;&quot;);
    }


int main()
{

    char arr[] = {'a','b','c','d','e','f'};
    int frequency[] = {5, 9, 12, 13, 16, 45};
    int size = sizeof(arr) / sizeof(arr[0]);
    HuffmanCodes(arr, frequency, size);
    return 0;
}