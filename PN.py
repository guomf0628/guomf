def possible_number_inference(grid):
    # 初始化结果为一个9x9的列表，每个元素初始化为空列表
    result = [[[] for _ in range(9)] for _ in range(9)]

    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:  # 如果单元格已有数字，直接使用该数字
                result[row][col] = [grid[row][col]]
                continue

            # 收集已使用的数字
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
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3
            for r_offset in range(3):
                for c_offset in range(3):
                    num = grid[box_row + r_offset][box_col + c_offset]
                    if num != 0:
                        used_numbers.add(num)

            # 确定候选数字
            candidates = [num for num in range(1, 10) if num not in used_numbers]
            result[row][col] = candidates

    return result


def format_output(candidates):
    # 将候选值列表转换为指定格式的字符串表示
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
