
# Data-Structure-Unit-5-Case-Study-

A Python case study demonstrating GPS navigation using weighted graphs and text compression using Huffman coding.

# GPS Navigation System and Huffman Compression

This project demonstrates two important applications of Data Structures:

1. GPS navigation using a weighted graph and Dijkstra's shortest-path algorithm.
2. Frequency-based text compression using a Huffman tree.

## Features

### GPS / Navigation System

- Represents a city map as a weighted graph.
- Stores connections and distances between cities.
- Finds the shortest route between two locations.
- Calculates the total distance of the selected route.
- Uses Dijkstra's algorithm.

### Huffman Compression

- Counts the frequency of each character.
- Builds a Huffman tree using a priority queue.
- Assigns binary codes to characters.
- Encodes the original text.
- Decodes the encoded text.
- Verifies that the original text is recovered correctly.

## Data Structures and Algorithms Used

### 1. Weighted Graph

A weighted graph consists of vertices and edges. Each edge has a weight representing distance, cost, or travel time.

In this project:
- Vertices represent cities.
- Edges represent roads.
- Edge weights represent distances in kilometres.

### 2. Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest paths from a starting vertex to other vertices in a weighted graph with non-negative edge weights.

The algorithm uses a priority queue to process the city with the smallest known distance first.

### 3. Huffman Tree

A Huffman tree is a binary tree used to generate variable-length binary codes based on character frequencies.

- Frequently occurring characters generally receive shorter codes.
- Less frequent characters generally receive longer codes.
- The codes are prefix-free, allowing unambiguous decoding.

### 4. Huffman Coding Algorithm

1. Count the frequency of every character.
2. Create a leaf node for each character.
3. Insert the nodes into a priority queue.
4. Remove the two nodes with the smallest frequencies.
5. Combine them into a new node.
6. Repeat until one tree remains.
7. Generate binary codes by traversing the tree.
8. Encode and decode the text.

## Requirements

- Python 3.7 or newer
- No external packages are required.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python CaseStudy5.py
   ```

If your system uses `python3`, run:

   ```bash
   python3 CaseStudy5.py
   ```

## Sample Output

See `sample_output.txt` for the complete program output.

### GPS Navigation

```text
Starting City: A
Destination City: E
Shortest Route: A -> C -> B -> D -> E
Total Distance: 10 km
```

### Huffman Compression

```text
Original Text: aaaaabcc
Encoded Text: 11111000101
Original Size: 64 bits
Encoded Size: 11 bits
Decoded Text: aaaaabcc
Lossless Verification: True
```

## Time Complexity

### GPS Navigation

Using an adjacency-list graph and a binary heap priority queue:

- Time Complexity: O((V + E) log V)
- Space Complexity: O(V + E)

Here, V is the number of vertices and E is the number of edges.

### Huffman Coding

Let n be the number of characters in the input and k be the number of distinct characters.

- Frequency counting: O(n)
- Huffman tree construction: O(k log k)
- Code generation: O(k)
- Encoding: O(n), excluding the cost of storing the encoded output
- Space Complexity: O(n + k), including stored input and encoded output

## Advantages

- Finds efficient routes through weighted graphs.
- Demonstrates practical graph algorithms.
- Reduces the number of bits required for some text inputs.
- Supports lossless encoding and decoding.
- Demonstrates the use of trees and priority queues.

## Limitations

- The navigation example uses a small sample city map, not live GPS data.
- Dijkstra's algorithm does not account for live traffic or changing road conditions.
- Huffman coding may not reduce every input's total file size once tree metadata and storage overhead are included.
- This program demonstrates Huffman coding but does not generate ZIP/GZIP-compatible compressed files.

## Applications

### GPS Navigation

- Route planning.
- Road network analysis.
- Delivery route planning.
- Transportation systems.

### Huffman Compression

- Lossless data compression.
- File storage and transmission.
- Data encoding.
- Compression algorithms and file formats.

## Conclusion

This case study demonstrates two important applications of Data Structures.

The navigation module uses a weighted graph and Dijkstra's algorithm to find a shortest route. The compression module uses character frequencies and a Huffman tree to encode and decode text.

Both examples illustrate how appropriate data structures and algorithms can solve practical computing problems.

## Files Included

- `CaseStudy5.py` - Python implementation of both modules.
- `sample_output.txt` - Sample program output.
- `README.md` - Case study documentation.

