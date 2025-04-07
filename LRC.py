def last_remaining_cell_inference(grid):
    # 用于存储每个单元格的候选值
    result = [[[] for _ in range(9)] for _ in range(9)]

    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:  # 已填入的单元格跳过
                result[row][col] = [grid[row][col]]  # 遍历棋盘
                continue

            used_numbers = set()

            # 检查行
            for c in range(9):
                if grid[row][c] != 0:
                    used_numbers.add(grid[row][c])

            # 检查列
            for r in range(9):
                if grid[r][col] != 0:
                    used_numbers.add(grid[r][col])

            # 检查宫格
            box_row_start = (row // 3) * 3
            box_col_start = (col // 3) * 3
            for r in range(box_row_start, box_row_start + 3):
                for c in range(box_col_start, box_col_start + 3):
                    if grid[r][c] != 0:
                        used_numbers.add(grid[r][c])

            # 找到候选值
            candidates = [num for num in range(1, 10) if num not in used_numbers]

            if len(candidates) == 1:
                grid[row][col] = candidates[0]
                result[row][col] = [candidates[0]]
            else:
                result[row][col] = candidates

    return result


# 正确的数独棋盘
sudoku_grid = [
    [2, 0, 0, 0, 7, 0, 0, 3, 8],
    [0, 0, 0, 0, 0, 6, 0, 7, 0],
    [3, 0, 0, 0, 4, 0, 6, 0, 0],
    [0, 0, 8, 0, 2, 0, 7, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 7, 0, 3, 0, 4, 0, 0],
    [0, 0, 4, 0, 8, 0, 0, 0, 9],
    [0, 6, 0, 4, 0, 0, 0, 0, 0],
    [9, 1, 0, 0, 6, 0, 0, 0, 2]
]

# 应用 LRC 策略并输出结果
result = last_remaining_cell_inference(sudoku_grid)

# 打印更新后的棋盘，以清晰的格式显示
for row in result:
    print(row)
