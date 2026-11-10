R, C = map(int, input().split(" "))
grid = [list(map(int, input().split(" "))) for _ in range(R)]

# TODO: result = the transposed grid (C rows of R numbers), negatives replaced by 0
#   hint: outer loop over columns, inner loop over rows, if/else in front
result = [[grid[j][i] if grid[j][i] > 0 else 0 for j in range(R)] for i in range(C)]
# TODO: positive = True only when every ORIGINAL cell is greater than 0
positive = all([grid[i][j] > 0 for i in range(R) for j in range(C)])

for row in result:
    print(*row)
print("all_positive:", "yes" if positive else "no")
