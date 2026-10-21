
# Case Study 5: GPS Navigation and Huffman Compression

import heapq


# MODULE 1: GPS / NAVIGATION USING A WEIGHTED GRAPH

def dijkstra(graph, start, destination):
    distances = {city: float("inf") for city in graph}
    previous = {city: None for city in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        distance, city = heapq.heappop(priority_queue)

        if distance > distances[city]:
            continue

        if city == destination:
            break

        for neighbor, weight in graph[city].items():
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = city
                heapq.heappush(
                    priority_queue, (new_distance, neighbor)
                )

    if distances[destination] == float("inf"):
        return [], float("inf")

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances[destination]


# MODULE 2: HUFFMAN TEXT COMPRESSION

class HuffmanNode:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right


def build_huffman_tree(text):
    if not text:
        return None

    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    heap = []
    counter = 0

    for char in sorted(frequency):
        node = HuffmanNode(char, frequency[char])
        heapq.heappush(heap, (node.frequency, counter, node))
        counter += 1

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        parent = HuffmanNode(None, freq1 + freq2, left, right)
        heapq.heappush(heap, (parent.frequency, counter, parent))
        counter += 1

    return heap[0][2]


def generate_codes(root):
    codes = {}

    def traverse(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code or "0"
            return

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")
    return codes


def encode_text(text, codes):
    return "".join(codes[char] for char in text)


def decode_text(encoded_text, root):
    if root is None:
        return ""

    # Special case: text contains only one unique character
    if root.char is not None:
        return root.char * len(encoded_text)

    decoded = []
    current = root

    for bit in encoded_text:
        current = current.left if bit == "0" else current.right

        if current.char is not None:
            decoded.append(current.char)
            current = root

    return "".join(decoded)


# MAIN PROGRAM

print("GPS NAVIGATION USING WEIGHTED GRAPH")

city_map = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2}
}

start = "A"
destination = "E"

path, distance = dijkstra(city_map, start, destination)

print("Starting City:", start)
print("Destination City:", destination)
print("Shortest Route:", " -> ".join(path))
print("Total Distance:", distance, "km")

print("\nHUFFMAN TEXT COMPRESSION")

text = "aaaaabcc"
root = build_huffman_tree(text)
codes = generate_codes(root)

encoded = encode_text(text, codes)
decoded = decode_text(encoded, root)

print("Original Text:", text)
print("Character Frequencies:")

for char in sorted(set(text)):
    print(f"{char}: {text.count(char)}")

print("Huffman Codes:")

for char in sorted(codes):
    print(f"{char}: {codes[char]}")

print("Encoded Text:", encoded)
print("Original Size:", len(text) * 8, "bits")
print("Encoded Size:", len(encoded), "bits")
print("Decoded Text:", decoded)
print("Lossless Verification:", decoded == text)
