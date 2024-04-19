field = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

round = 0

def show():
    print("   0 1 2")
    print("_" * 8)
    for column, row in enumerate(field):
        field_game = f"{column}| {" ".join(row)}"
        print(field_game)

def turn():
    while True:
        enter = input("Введите значения {строка} {колонка}: ").split()
        if len(enter) != 2:
            print("Значения нужно записать 2 через пробел!")
            continue

        column, row = enter

        if not (column.isdigit()) or not(row.isdigit()):
            print("Введено не число! Нужно ввести 2 числа через пробел от 1-3 {число} {число} ")
            continue

        column, row = int(column), int(row)

        if 0 > column or column > 2 and 0 > row or row > 2:
            print("Данные введены не верно! Введите число от 1-3 {число} {число}")
            continue

        if field[column][row] != "-":
            print("Колонка занята")
            continue

        return column, row



def win():
    _combo = (((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)), ((0,0),(1,0),(2,0)),((0,2),(1,1),(2,0)),
              ((0,0),(1,1),(2,2)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)))

    for combo in _combo:
        set_win = []
        for c in combo:
            set_win.append(field[c[0]][c[1]])
        if set_win == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if set_win == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False



while True:

    round += 1
    show()
    if round % 2 == 1:
        print(f"Ход {round}, ход крестика")
    else:
        print(f"Ход {round}, ход нолика")

    column, row = turn()

    if round % 2 == 1:
        field[column][row] = "X"
    else:
        field[column][row] = "0"

    if win():
        print("_"* 8)
        print("Конец игры!")
        break

    if round == 9:
        print("Ничья!")
        break