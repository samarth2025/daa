import heapq

class Node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = '' 

    def __lt__(self, nxt): 
        return self.freq < nxt.freq 

def printNodes(node, val=''): 
    newVal = val + str(node.huff)
    if node.left: 
        printNodes(node.left, newVal)
    if node.right: 
        printNodes(node.right, newVal)
    if not node.left and not node.right: 
        print(f"{node.symbol} -> {newVal}")

# User input for characters and frequencies
chars = list(input("Enter the characters (e.g., 'abcdef'): "))
freq = list(map(int, input("Enter the frequencies (space-separated, e.g., '5 9 12 13 16 45'): ").split()))

# Create a priority queue using the characters and their frequencies
nodes = []
for x in range(len(chars)): 
    heapq.heappush(nodes, Node(freq[x], chars[x])) 

# Build the Huffman Tree
while len(nodes) > 1: 
    left = heapq.heappop(nodes) 
    right = heapq.heappop(nodes) 

    left.huff = 0
    right.huff = 1

    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right) 
    heapq.heappush(nodes, newNode) 

# Print the Huffman codes
print("Huffman Codes for each character:")
printNodes(nodes[0])
