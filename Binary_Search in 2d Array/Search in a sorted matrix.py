#Search in a sorted matrix.py
matrix = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12],
 [13,14,15,16]
]

Target = 10

row = 0
col = len(matrix[0]) - 1  # start from top-right corner

while row < len(matrix) and col >= 0:
    current = matrix[row][col]
    if current == Target:
        print(f"Found {Target} at position ({row}, {col})")
        break
    elif current < Target:
        row+= 1  
    else:
        col -= 1  
else:
    print("Not found")