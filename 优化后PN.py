def get_existing_numbers(grid, row, col):
    """获取指定单元格所在行、列和宫格已经存在的数字"""
    existing_numbers = set()

    # 检查行
    existing_numbers.update(grid[row])

    # 检查列
    existing_numbers.update(grid[i][col] for i in range(9))

    # 检查3x3宫格
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            existing_numbers.add(grid[i][j])

    return existing_numbers


def get_candidates(grid, row, col):
    """获取指定单元格的候选数字"""
    if grid[row][col] != 0:
        return [grid[row][col]]
    existing_numbers = get_existing_numbers(grid, row, col)
    # 找到候选值
    return [num for num in range(1, 10) if num not in existing_numbers]


def possible_number_inference(grid):
    """推断数独中每个单元格的候选值"""
    result = [[[] for _ in range(9)] for _ in range(9)]

    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:  # 如果单元格已有数字，直接使用该数字
                result[row][col] = [grid[row][col]]
            else:
                candidates = get_candidates(grid, row, col)
                if len(candidates) == 1:
                    grid[row][col] = candidates[0]  # 如果只有一个候选值，填入该值
                    result[row][col] = [candidates[0]]
                else:
                    result[row][col] = candidates  # 否则，列出所有候选值

    return result


def format_output(candidates):
    """将候选值列表转换为指定格式的字符串表示"""
    formatted = []  # 二维列表
    for row in candidates:
        formatted_row = []
        for cell in row:
            if len(cell) == 1:
                formatted_row.append(f"[{cell[0]}]")
            else:
                formatted_row.append("[" + ", ".join(map(str, cell)) + "]")
        formatted.append(formatted_row)
    return formatted


def print_formatted(formatted):
    """打印格式化后的候选值"""
    for row in formatted:
        print("[" + ", ".join(row) + "]")


# 输入的数独网格
grid = [
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

if __name__ == "__main__":
    candidates = possible_number_inference(grid)
    formatted = format_output(candidates)
    print_formatted(formatted)
