def longest_consecutive_path(matrix, start_char):
    def dfs(i, j, curr_len, longest_len):
        longest_len = max(longest_len, curr_len)
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if (ni, nj) in visited or not (0 <= ni < rows and 0 <= nj < cols) or matrix[ni][nj] != chr(ord(curr_char) + 1):
                continue
            visited.add((ni, nj))
            longest_len = dfs(ni, nj, curr_len + 1, longest_len)
            visited.remove((ni, nj))
        return longest_len

    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    visited = set()
    longest_len = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                curr_char = start_char
                visited.add((i, j))
                longest_len = dfs(i, j, 1, longest_len)
                visited.remove((i, j))

    return longest_len


input_rows = 5
input_matrix = [
    ['D', 'E', 'H', 'X', 'B'],
    ['A', 'O', 'G', 'P', 'E'],
    ['D', 'D', 'C', 'F', 'D'],
    ['E', 'B', 'E', 'A', 'S'],
    ['C', 'D', 'Y', 'E', 'N']
]
start_char = 'C'

result = longest_consecutive_path(input_matrix, start_char)
print(f"The length of the longest path with consecutive characters starting from character {start_char} is {result}")
