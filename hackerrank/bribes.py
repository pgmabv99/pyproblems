def minimum_bribes(q):
    bribes = 0
    for i in range(len(q)):
        iold=q[i]-1
        print(i, iold)
        if i - iold  > 2:  # Check if any person has bribed more than two others
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):  # Check how many times person i has been bribed
            if q[j] > q[i]:
                bribes += 1
    print(bribes)

# Example usage:
# queue = [2, 1, 5, 3, 4]  # Example queue order
# queue = [2, 3, 5, 4 , 1]  # Example queue order
#        1,2,3,4,5

queue = [2,5,1,3,4]  # Example queue order
minimum_bribes(queue)
