import heapq

# Create an empty list to represent the heap
min_heap = []

# Push elements onto the heap
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)

print("Min heap after pushing elements:", min_heap)

# Pop the smallest element from the heap
smallest = heapq.heappop(min_heap)
print("Smallest element popped from min heap:", smallest)
print("Min heap after popping smallest element:", min_heap)
