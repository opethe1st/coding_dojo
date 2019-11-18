

def mineswepper_solver():
    NUMBER_OF_FIELDS = 2
    for field_number in range(1, NUMBER_OF_FIELDS + 1):
        print(f"Field #{field_number}")
        field = ""
        n, m = map(int, input().split())
        for row in range(n):
            field += input() + "\n"

        print(solution(field))
        print()


def solution(field):
    field = field.strip()
    field = field.split('\n')

    ans = []
    for i, field_row in enumerate(field):
        row = []
        for j, item in enumerate(field_row):
            row.append(
                number_of_neighboring_mines((i, j), field)
            )
        ans.append(row)
    res = "\n".join("".join([str(item) for item in row]) for row in ans)
    return res


def number_of_neighboring_mines(position, field):
    number_of_rows = len(field)
    number_of_columns = len(field[0])
    x, y = position
    if field[x][y] == '*':
        return '*'
    else:
        # 0, 0 -> (0, 1), (1, 1), (1, 0)
        # 1, 1 -> (0, 0), (0, 1), (0, 2), (1, 2),
        number_of_mines = 0
        for xdirection in [-1, 0, 1]:
            for ydirection in [-1, 0, 1]:
                if (0 <= x + xdirection < number_of_rows) and (0 <= y + ydirection < number_of_columns):
                    if field[x + xdirection][y + ydirection] == '*':
                        number_of_mines += 1
        return number_of_mines


if __name__ == "__main__":
    # field = [
    #     '*...',
    #     '....',
    #     '.*..',
    #     '....',
    # ]
    # print(number_of_neighboring_mines((1, 0), field))
    # print(solution(field= "*...\n....\n.*..\n...."))
    mineswepper_solver()
