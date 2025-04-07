def get_existing_numbers(sudoku_grid, row, col):
    existing_numbers = set()
    # 检查行
    existing_numbers.update(sudoku_grid[row])
    # 检查列
    existing_numbers.update(sudoku_grid[i][col] for i in range(9))
    # 检查3x3宫格
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            existing_numbers.add(sudoku_grid[i][j])
    return existing_numbers

def get_candidates(grid, row, col):
    if grid[row][col] != 0:
        return [grid[row][col]]
    existing_numbers = get_existing_numbers(grid, row, col)
    # 找到候选值
    return [num for num in range(1, 10) if num not in existing_numbers]

def last_remaining_cell_inference(grid):
    """推断数独中每个单元格的候选值"""
    result = [[[] for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                result[row][col] = [grid[row][col]]
                continue
            candidates = get_candidates(grid, row, col)
            if len(candidates) == 1:
                grid[row][col] = candidates[0]
                result[row][col] = [candidates[0]]
            else:
                result[row][col] = candidates
    return result

def is_valid_sudoku(sudoku_grid):
    """验证数独网格是否有效"""
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] != 0:
                # 检查行中是否有重复
                if sudoku_grid[row].count(sudoku_grid[row][col]) > 1:
                    return False
                # 检查列中是否有重复
                if any(sudoku_grid[i][col] == sudoku_grid[row][col] for i in range(9) if i != row):
                    return False
                # 检查3x3宫格是否有重复
                box_row_start = (row // 3) * 3
                box_col_start = (col // 3) * 3
                for i in range(box_row_start, box_row_start + 3):
                    for j in range(box_col_start, box_col_start + 3):
                        if (i != row or j != col) and sudoku_grid[i][j] == sudoku_grid[row][col]:
                            return False
    return True

# 输入的数独网格，确保每行都是有效的，并且包含九个元素
sudoku_grid = [
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,8 ,1 ,9],  # 示例行
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]   # 示例行
]

# 验证输入的数独棋盘是否有效
if is_valid_sudoku(sudoku_grid):
    # 应用 LRC 策略并输出结果
    result = last_remaining_cell_inference(sudoku_grid)
    # 打印更新后的棋盘，以清晰的格式显示
    for row in result:
        print(row)
else:
    print("输入的数独网格无效！")
