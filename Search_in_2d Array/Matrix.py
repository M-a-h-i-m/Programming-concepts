matrix = [
  [10, 20, 30, 40],
  [11, 21, 31, 41],
  [12, 22, 32, 33],
  [13, 23, 33, 43]
]

Target = 22

row = 0
col = len(matrix[0]) - 1  # start from top-right corner

while row < len(matrix) and col >= 0:
    current = matrix[row][col]
    if current == Target:
        print(f"Found {Target} at position ({row}, {col})")
        break
    elif current > Target:
        col -= 1  # move left
    else:
        row += 1  # move down
else:
    print("Not found")
