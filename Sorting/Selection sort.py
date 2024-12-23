# Time complexity: O(n**2)
array = [1, 2, 5, 4, 6, 3, 7, 9, 8]

for i in range(len(array) - 1):
    pos = i
    for j in range(i + 1, len(array)):
        if array[j] < array[pos]:
            pos = j
    array[i], array[pos] = array[pos], array[i]

print(array)
